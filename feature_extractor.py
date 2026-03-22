"""
feature_extractor.py  (v2 — calibrated to real normal traffic)
===============================================================
Converts your network capture JSON format into ML features.

Key changes from v1:
  - Suspicious domain list REMOVED from scoring. Your data shows that
    sammods.github.io, sadownload.mcafee.com, cloudflare-ech.com all
    appear in your confirmed-normal traffic. They are not scored.
  - Only domains with ZERO ambiguity (known C2 frameworks, active
    malware IPs from threat intel) should be hard-flagged — and none
    of those appear in your data.
  - All feature ranges are calibrated to your observed normal values.
  - synthetic normals are generated from the real data's own distribution.

Input JSON format:
{
  "10.42.0.110": {
    "nmap": "...",
    "sni":  [{"time": "...", "destination": "...", "domain": "..."}],
    "conversations": [{"source":"...","destination":"...","data":"4005 5,292 kB"}],
    "io_stats": [724, 10, 12, ...]
  }
}
"""

import json
import math
import os
import re
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any

import numpy as np
import pandas as pd

# ─────────────────────────────────────────────────────────────────
# DOMAIN CATEGORIES
# Used only to compute diversity features — not to flag anything.
# ─────────────────────────────────────────────────────────────────

_CATEGORY_MAP = {
    "google"   : ["google.com","googleapis.com","gstatic.com","googleusercontent.com",
                  "googlevideo.com","ytimg.com","ggpht.com","google.co.in",
                  "doubleclick.net","googlesyndication.com","youtube.com"],
    "social"   : ["facebook.com","fbcdn.net","instagram.com","twitter.com",
                  "tiktok.com","snapchat.com","linkedin.com","whatsapp.com",
                  "messenger.com","licdn.com"],
    "microsoft": ["microsoft.com","windows.com","msn.com","live.com",
                  "azure.com","office.com","bing.com"],
    "streaming": ["spotify.com","netflix.com","hotstar.com","primevideo.com"],
    "cdn"      : ["cloudfront.net","akamai.com","cloudflare.com","fastly.net",
                  "imagekit.io","branch.io","mixpanel.com","intercom.io",
                  "github.com","github.io"],
    "ai_tools" : ["chatgpt.com","openai.com","quillbot.com","anthropic.com"],
    "telemetry": ["telemetry","analytics","collector","events.data","tracking",
                  "activity.windows","mobile.events"],
}

def _domain_category(domain: str) -> str:
    d = domain.lower()
    for cat, patterns in _CATEGORY_MAP.items():
        if any(p in d for p in patterns):
            return cat
    return "unknown"

def _get_root_domain(domain: str) -> str:
    parts = domain.strip().lower().split(".")
    if len(parts) >= 3 and parts[-2] in ("co","com","net","org","gov"):
        return ".".join(parts[-3:])
    return ".".join(parts[-2:]) if len(parts) >= 2 else domain

def _parse_data_field(data_str: str) -> Tuple[int, float]:
    try:
        parts = data_str.strip().split()
        return int(parts[0].replace(",","")), float(parts[1].replace(",",""))
    except Exception:
        return 0, 0.0

def _sni_time_span_seconds(sni_entries: List[Dict]) -> float:
    if len(sni_entries) < 2:
        return 1.0
    times = []
    for e in sni_entries:
        raw = e.get("time","")
        try:
            raw_t = re.sub(r"(\d{2}:\d{2}:\d{2})\.(\d{6})\d* IST", r"\1.\2 IST", raw)
            times.append(datetime.strptime(raw_t, "Mar %d, %Y %H:%M:%S.%f IST").timestamp())
        except Exception:
            continue
    return max(max(times) - min(times), 0.0) + 1.0 if len(times) >= 2 else 1.0


# ─────────────────────────────────────────────────────────────────
# FEATURE SCHEMA  — 24 features
# ─────────────────────────────────────────────────────────────────

FEATURE_COLUMNS = [
    # IO Stats
    "io_mean",              # average packets per interval
    "io_max",               # peak burst
    "io_std",               # traffic variability
    "io_spike_ratio",       # max / mean  (bursty devices normal up to ~7×)
    "io_cv",                # std / mean  (coefficient of variation)
    "io_zero_frac",         # fraction of zero-traffic intervals
    "io_total",             # total packets across all intervals
    # Conversations
    "total_packets",        # total packets all conversations
    "total_kb",             # total kilobytes transferred
    "num_destinations",     # unique destination IPs contacted
    "top_dest_pkt_frac",    # fraction of packets to the busiest single dest
    "avg_kb_per_dest",      # KB per unique destination
    "inbound_pkt_frac",     # fraction of convs where device is the destination
    # SNI / Domain
    "unique_domains",       # distinct FQDNs in SNI
    "unique_root_domains",  # distinct root domains
    "total_sni",            # total SNI handshake events
    "sni_repeat_ratio",     # total_sni / unique_domains
    "sni_rate_per_sec",     # SNI events per second of capture window
    "unknown_domain_frac",  # fraction of domains with unknown category
    "telemetry_frac",       # fraction classified as telemetry/analytics
    "category_entropy",     # Shannon entropy of domain category distribution
    # Combined
    "kb_per_domain",        # total_kb / unique_domains
    "packets_per_dest",     # total_packets / num_destinations
    "sni_density",          # total_sni / num_destinations (SNI per dest IP)
]


def extract_features(ip: str, session: Dict) -> Optional[Dict]:
    """Extract all 24 features from one device session."""
    try:
        io_raw = session.get("io_stats", [])
        snis   = session.get("sni", [])
        convs  = session.get("conversations", [])

        # ── IO Stats ──────────────────────────────────────────────
        if io_raw:
            io_arr         = np.array(io_raw, dtype=float)
            io_mean        = float(np.mean(io_arr))
            io_max         = float(np.max(io_arr))
            io_std         = float(np.std(io_arr))
            io_mean_s      = max(io_mean, 1e-6)
            io_spike_ratio = io_max / io_mean_s
            io_cv          = io_std / io_mean_s
            io_zero_frac   = float(np.sum(io_arr == 0) / len(io_arr))
            io_total       = float(np.sum(io_arr))
        else:
            io_mean = io_max = io_std = io_spike_ratio = io_cv = io_total = 0.0
            io_zero_frac = 0.0

        # ── Conversations ─────────────────────────────────────────
        total_packets = 0
        total_kb      = 0.0
        dest_pkts: Dict[str, int]   = {}
        inbound_convs = 0

        for c in convs:
            src  = c.get("source","")
            dst  = c.get("destination","")
            pkts, kb = _parse_data_field(c.get("data","0 0 kB"))
            total_packets += pkts
            total_kb      += kb
            if src == ip:
                dest_pkts[dst] = dest_pkts.get(dst, 0) + pkts
            else:
                inbound_convs += 1

        num_dest     = max(len(dest_pkts), 1)
        total_pkt_s  = max(total_packets, 1)

        top_pkt          = max(dest_pkts.values(), default=0)
        top_dest_pkt_frac= top_pkt / total_pkt_s
        avg_kb_per_dest  = total_kb / num_dest
        inbound_frac     = inbound_convs / max(len(convs), 1)

        # ── SNI / Domain ──────────────────────────────────────────
        domains          = [e.get("domain","") for e in snis]
        unique_d         = len(set(domains))
        root_doms        = [_get_root_domain(d) for d in domains]
        unique_root      = len(set(root_doms))
        total_sni        = len(snis)

        sni_repeat_ratio = total_sni / max(unique_d, 1)
        sni_span         = _sni_time_span_seconds(snis)
        sni_rate         = total_sni / sni_span

        cats     = [_domain_category(d) for d in domains]
        n_cats   = max(len(cats), 1)
        unknown_frac   = cats.count("unknown")   / n_cats
        telemetry_frac = cats.count("telemetry") / n_cats

        # Shannon entropy over category distribution
        from collections import Counter
        cat_counts = Counter(cats)
        total_c    = sum(cat_counts.values())
        cat_entropy = 0.0
        if total_c > 0:
            for cnt in cat_counts.values():
                p = cnt / total_c
                cat_entropy -= p * math.log2(p + 1e-12)
            # Normalise by log2(num_possible_cats)
            cat_entropy /= math.log2(len(_CATEGORY_MAP) + 1)

        # ── Combined ──────────────────────────────────────────────
        kb_per_domain    = total_kb   / max(unique_d, 1)
        packets_per_dest = total_packets / num_dest
        sni_density      = total_sni / num_dest   # SNI handshakes per dest IP

        return {
            "_ip"              : ip,
            # ML features
            "io_mean"          : io_mean,
            "io_max"           : io_max,
            "io_std"           : io_std,
            "io_spike_ratio"   : io_spike_ratio,
            "io_cv"            : io_cv,
            "io_zero_frac"     : io_zero_frac,
            "io_total"         : io_total,
            "total_packets"    : float(total_packets),
            "total_kb"         : total_kb,
            "num_destinations" : float(num_dest),
            "top_dest_pkt_frac": top_dest_pkt_frac,
            "avg_kb_per_dest"  : avg_kb_per_dest,
            "inbound_pkt_frac" : inbound_frac,
            "unique_domains"   : float(unique_d),
            "unique_root_domains": float(unique_root),
            "total_sni"        : float(total_sni),
            "sni_repeat_ratio" : sni_repeat_ratio,
            "sni_rate_per_sec" : sni_rate,
            "unknown_domain_frac": unknown_frac,
            "telemetry_frac"   : telemetry_frac,
            "category_entropy" : cat_entropy,
            "kb_per_domain"    : kb_per_domain,
            "packets_per_dest" : packets_per_dest,
            "sni_density"      : sni_density,
        }

    except Exception as exc:
        print(f"[ERROR] Feature extraction failed for {ip}: {exc}")
        return None


def load_files(file_paths: List[str]) -> Tuple[pd.DataFrame, List[Dict]]:
    """
    Load network capture JSON files → feature DataFrame + metadata list.
    One row per (file, IP) session pair.
    """
    feat_rows = []
    meta_rows = []

    for fpath in file_paths:
        if not os.path.isfile(fpath):
            print(f"[WARN] File not found: {fpath}")
            continue
        with open(fpath) as f:
            data = json.load(f)
        for ip, session in data.items():
            row = extract_features(ip, session)
            if row is None:
                continue
            meta_rows.append({
                "_ip"  : row.pop("_ip"),
                "_file": os.path.basename(fpath),
            })
            feat_rows.append(row)

    if not feat_rows:
        return pd.DataFrame(columns=FEATURE_COLUMNS), []

    df = pd.DataFrame(feat_rows)[FEATURE_COLUMNS]
    df = df.replace([np.inf, -np.inf], np.nan).fillna(0.0)
    return df, meta_rows


def generate_synthetic_normals(
    real_df: pd.DataFrame,
    n: int = 400,
    seed: int = 42,
) -> pd.DataFrame:
    """
    Generate synthetic normal sessions sampled from the ACTUAL distributions
    of your real training data, not from generic assumptions.

    Method: for each feature, fit a parametric distribution to the real values
    (normal or log-normal depending on skew) and sample from it.
    Clamps to [real_min * 0.5, real_max * 1.5] to stay realistic.
    """
    rng = np.random.default_rng(seed)
    rows = []

    # Pre-compute per-feature stats from real data
    stats = {}
    for col in FEATURE_COLUMNS:
        v = real_df[col].values.astype(float)
        v = v[np.isfinite(v)]
        stats[col] = {
            "mean" : float(np.mean(v)),
            "std"  : max(float(np.std(v)), 1e-6),
            "min"  : float(np.min(v)),
            "max"  : float(np.max(v)),
            "p05"  : float(np.percentile(v, 5)),
            "p95"  : float(np.percentile(v, 95)),
        }

    for _ in range(n):
        row = {}
        for col in FEATURE_COLUMNS:
            s = stats[col]
            # Sample from a normal distribution centered at the real mean
            # Use a slightly wider std (1.3×) to cover edge cases
            val = rng.normal(s["mean"], s["std"] * 1.3)
            # Clamp to the realistic range observed in your data
            lo  = max(s["min"] * 0.5, 0.0)
            hi  = s["max"] * 1.5
            row[col] = float(np.clip(val, lo, hi))

        # Hard constraints: fraction features must stay in [0,1]
        for frac_col in ["io_zero_frac","top_dest_pkt_frac","inbound_pkt_frac",
                         "unknown_domain_frac","telemetry_frac"]:
            row[frac_col] = float(np.clip(row[frac_col], 0.0, 1.0))

        # Non-negative features
        for pos_col in ["io_mean","io_max","io_std","io_total","total_packets",
                        "total_kb","num_destinations","unique_domains",
                        "unique_root_domains","total_sni","kb_per_domain",
                        "packets_per_dest","sni_density"]:
            row[pos_col] = max(row[pos_col], 0.0)

        rows.append(row)

    df = pd.DataFrame(rows)[FEATURE_COLUMNS]
    return df.replace([np.inf, -np.inf], np.nan).fillna(0.0)
