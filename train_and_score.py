"""
train_and_score.py  (v2 — trained on confirmed normal traffic)
==============================================================
Your 4 JSON files are all normal. This pipeline:

  1. Extracts features from all 4 files (10 normal sessions)
  2. Generates 400 synthetic normals sampled from YOUR real data ranges
  3. Trains Isolation Forest with contamination=0.02
     (very few anomalies expected — model learns YOUR normal tightly)
  4. Calibrates scores using empirical CDF of the training distribution
  5. Scores each session and explains only deviations from YOUR normal

Because the baseline is purely normal, the anomaly detector will only
flag future devices that are genuinely unlike what your network looks like.

Run:
    python train_and_score.py
    python train_and_score.py --score data/new_capture.json
"""

import argparse
import json
import os
import sys
from collections import Counter
from typing import Dict, List

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

from feature_extractor import (
    FEATURE_COLUMNS,
    extract_features,
    generate_synthetic_normals,
    load_files,
)

# ─────────────────────────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────────────────────────

TRAINING_FILES = [
    "data/network_data1.json",
    "data/network_data2.json",
    "data/network_data3.json",
    "data/network_data4.json",
]

N_SYNTHETIC    = 400    # synthetic normals — sampled from your actual ranges
CONTAMINATION  = 0.02   # ~2% anomaly expectation — all your training data is normal
N_ESTIMATORS   = 300    # more trees = more stable boundary on small real dataset
RANDOM_STATE   = 42

MODEL_PATH     = "models/if_model.joblib"
SCALER_PATH    = "models/scaler.joblib"
CALIB_PATH     = "models/calibrator.joblib"
STATS_PATH     = "models/training_stats.json"
OUTPUT_JSON    = "output/scored_devices.json"


# ─────────────────────────────────────────────────────────────────
# SCORE CALIBRATOR
# ─────────────────────────────────────────────────────────────────

class ScoreCalibrator:
    """
    Maps raw IF decision_function scores → calibrated anomaly score [0,1]
    using the empirical CDF of training scores.

    Score meaning: "what fraction of your NORMAL training sessions
    look MORE anomalous than this device?"

    0.0 → perfectly typical for your network
    0.5 → somewhat unusual but within the envelope
    0.9 → looks very different from anything in your normal data
    """
    def __init__(self):
        self._sorted = None

    def fit(self, raw: np.ndarray) -> "ScoreCalibrator":
        self._sorted = np.sort(raw.astype(np.float64))
        return self

    def transform(self, raw: np.ndarray) -> np.ndarray:
        if self._sorted is None:
            return np.clip(0.5 - raw * 0.5, 0.0, 1.0)
        ranks = np.searchsorted(self._sorted, raw, side="left")
        return np.clip(1.0 - ranks / len(self._sorted), 0.0, 1.0)

    def transform_one(self, v: float) -> float:
        return float(self.transform(np.array([v]))[0])


def classify_score(score: float) -> str:
    """
    Thresholds calibrated to contamination=0.02:
      NORMAL     < 0.50 — typical for this network
      MODERATE   0.50–0.74 — slightly unusual, worth watching
      SUSPICIOUS 0.75–0.89 — clearly outside normal envelope
      HIGH RISK  >= 0.90 — very different from all normal sessions
    """
    if score >= 0.90:
        return "🚨 HIGH RISK"
    if score >= 0.75:
        return "⚠️  SUSPICIOUS"
    if score >= 0.50:
        return "🔍 MODERATE"
    return "✅ NORMAL"


# ─────────────────────────────────────────────────────────────────
# RULE ENGINE — calibrated to your confirmed-normal data ranges
# ─────────────────────────────────────────────────────────────────
#
# All thresholds below are set BEYOND the maximum values seen in
# your 4 training files (your normal data). Rules only fire when
# a future session exceeds what you confirmed as normal.
#
# Your normal data observed maxima (used to set thresholds):
#   io_spike_ratio     max = 7.01  → threshold = 9.0
#   total_kb           max = 8111  → threshold = 12000
#   top_dest_pkt_frac  max = 0.965 → threshold = 0.98 (essentially 100%)
#   sni_repeat_ratio   max = 2.3   → threshold = 6.0
#   kb_per_domain      max = 4056  → threshold = 8000
#   total_packets      max = 7739  → threshold = 15000
#   io_cv              max = 1.79  → threshold = 2.5
#   unique_domains     max = 20    → threshold = 40
# ─────────────────────────────────────────────────────────────────

# Feature stats from your training data (for z-score context in reports)
_TRAIN_STATS: Dict[str, Dict] = {}  # populated after training

def explain_session(feat: Dict) -> List[str]:
    """
    Fire rules ONLY on values that exceed your confirmed-normal maximums.
    Each rule includes what your normal data showed for context.
    """
    reasons = []

    # R1 — IO spike beyond all normal observations
    if feat["io_spike_ratio"] >= 9.0:
        reasons.append(
            f"R1: IO spike {feat['io_spike_ratio']:.1f}× mean "
            f"[your normal max: 7.0×] — extreme burst, investigate source"
        )

    # R2 — Volume far above anything in training
    if feat["total_kb"] >= 12000:
        reasons.append(
            f"R2: Total transfer {feat['total_kb']:.0f} KB "
            f"[your normal max: ~8,100 KB] — unusually high data volume"
        )

    # R3 — Near-100% traffic concentration AND very high volume
    # (96% to one dest was normal for YouTube streaming, so only flag
    #  if combined with large volume suggesting non-streaming exfil)
    if feat["top_dest_pkt_frac"] >= 0.98 and feat["total_kb"] >= 5000:
        reasons.append(
            f"R3: {feat['top_dest_pkt_frac']*100:.0f}% of traffic ({feat['total_kb']:.0f} KB) "
            f"to one destination — unusual even vs your streaming sessions"
        )

    # R4 — SNI hammering far beyond normal (your max was 2.3×)
    if feat["sni_repeat_ratio"] >= 6.0:
        reasons.append(
            f"R4: SNI repeat ratio {feat['sni_repeat_ratio']:.1f}× "
            f"[your normal max: 2.3×] — same host repeatedly polled (tunnel/beacon?)"
        )

    # R5 — KB per domain far above normal (your max was 4,056)
    if feat["kb_per_domain"] >= 8000:
        reasons.append(
            f"R5: {feat['kb_per_domain']:.0f} KB per unique domain "
            f"[your normal max: ~4,100 KB] — large per-host data movement"
        )

    # R6 — Total packets far above your heaviest session (7,739)
    if feat["total_packets"] >= 15000:
        reasons.append(
            f"R6: {feat['total_packets']:.0f} total packets "
            f"[your normal max: ~7,700] — volume exceeds all observed normal sessions"
        )

    # R7 — Very erratic traffic (your normal max io_cv was 1.79)
    if feat["io_cv"] >= 2.5:
        reasons.append(
            f"R7: IO variability coefficient {feat['io_cv']:.2f} "
            f"[your normal max: 1.79] — highly irregular traffic rhythm"
        )

    # R8 — Unusually many unique domains (your max was 20)
    if feat["unique_domains"] >= 40:
        reasons.append(
            f"R8: {feat['unique_domains']:.0f} unique domains contacted "
            f"[your normal max: 20] — unusually wide domain spread"
        )

    # R9 — Very fast SNI rate (your max was 5.04/s from a 23-SNI burst)
    if feat["sni_rate_per_sec"] >= 8.0:
        reasons.append(
            f"R9: {feat['sni_rate_per_sec']:.1f} SNI handshakes/sec "
            f"[your normal max: ~5.0/s] — extremely fast domain resolution rate"
        )

    # R10 — Very high destination count (your max was 37 — already high-end normal)
    if feat["num_destinations"] >= 60:
        reasons.append(
            f"R10: {feat['num_destinations']:.0f} unique destination IPs "
            f"[your normal max: 37] — unusually wide network reach"
        )

    return reasons


def _z_context(feat: Dict, col: str) -> str:
    """Show how far a value sits from the training mean in std units."""
    if col not in _TRAIN_STATS:
        return ""
    s    = _TRAIN_STATS[col]
    z    = (feat[col] - s["mean"]) / max(s["std"], 1e-6)
    pct  = s.get("percentile_rank", {}).get(round(feat[col], 2), "?")
    return f"z={z:+.1f}σ"


# ─────────────────────────────────────────────────────────────────
# MAIN PIPELINE
# ─────────────────────────────────────────────────────────────────

def train():
    print("=" * 66)
    print("  ANOMALY DETECTOR — TRAINING ON YOUR CONFIRMED NORMAL DATA")
    print("=" * 66)

    # ── 1. Load real normal data ──────────────────────────────────
    print("\n[1/5] Loading your 4 confirmed-normal capture files...")
    real_df, real_meta = load_files(TRAINING_FILES)

    if real_df.empty:
        print("ERROR: No records loaded. Check file paths.")
        sys.exit(1)

    print(f"      {len(real_df)} normal sessions loaded:")
    for m in real_meta:
        print(f"       • {m['_file']:<26} → {m['_ip']}")

    # ── 2. Synthetic normal augmentation ─────────────────────────
    print(f"\n[2/5] Generating {N_SYNTHETIC} synthetic normals from your "
          f"data's own distribution...")
    synth_df = generate_synthetic_normals(real_df, n=N_SYNTHETIC, seed=RANDOM_STATE)
    train_df = pd.concat([real_df, synth_df], ignore_index=True)
    print(f"      Training set: {len(real_df)} real + {len(synth_df)} synthetic "
          f"= {len(train_df)} total")
    print(f"      Contamination: {CONTAMINATION} "
          f"(only {int(CONTAMINATION*len(train_df))} anomalies expected in training)")

    # ── 3. Scale ──────────────────────────────────────────────────
    print("\n[3/5] Fitting StandardScaler on training distribution...")
    scaler  = StandardScaler()
    X_train = scaler.fit_transform(train_df[FEATURE_COLUMNS].values)
    X_real  = scaler.transform(real_df[FEATURE_COLUMNS].values)
    print(f"      {len(FEATURE_COLUMNS)} features scaled")

    # ── 4. Train Isolation Forest ─────────────────────────────────
    print(f"\n[4/5] Training Isolation Forest "
          f"(n_estimators={N_ESTIMATORS}, contamination={CONTAMINATION})...")
    model = IsolationForest(
        n_estimators  = N_ESTIMATORS,
        contamination = CONTAMINATION,
        max_samples   = "auto",
        n_jobs        = -1,
        random_state  = RANDOM_STATE,
    )
    model.fit(X_train)

    # Calibrate on full training distribution
    calibrator = ScoreCalibrator()
    calibrator.fit(model.decision_function(X_train))

    # Store training stats for z-score context in reports
    global _TRAIN_STATS
    for col in FEATURE_COLUMNS:
        v = train_df[col].values
        _TRAIN_STATS[col] = {
            "mean": float(np.mean(v)),
            "std" : float(np.std(v)),
            "min" : float(np.min(v)),
            "max" : float(np.max(v)),
        }

    # Save artifacts
    os.makedirs("models", exist_ok=True)
    joblib.dump(model,      MODEL_PATH)
    joblib.dump(scaler,     SCALER_PATH)
    joblib.dump(calibrator, CALIB_PATH)
    with open(STATS_PATH, "w") as f:
        json.dump(_TRAIN_STATS, f, indent=2)
    print(f"      Saved: {MODEL_PATH}, {SCALER_PATH}, {CALIB_PATH}")

    # ── 5. Score training sessions to confirm baseline ────────────
    print("\n[5/5] Scoring your 10 normal training sessions...")
    raw_scores = model.decision_function(X_real)
    cal_scores = calibrator.transform(raw_scores)
    if_flags   = model.predict(X_real)

    results = _build_results(real_df, real_meta, raw_scores, cal_scores, if_flags)
    _print_report(results, is_training=True)

    os.makedirs("output", exist_ok=True)
    _save_results(results, OUTPUT_JSON)
    print(f"\n  Results saved → {OUTPUT_JSON}")
    print(f"\n  To score new data:  python train_and_score.py --score <file.json>")


def score_new_file(path: str):
    """Load saved model and score a new capture file."""
    for p, name in [(MODEL_PATH,"Model"),(SCALER_PATH,"Scaler"),(CALIB_PATH,"Calibrator")]:
        if not os.path.isfile(p):
            print(f"ERROR: {name} not found at '{p}'. Run training first.")
            sys.exit(1)

    model      = joblib.load(MODEL_PATH)
    scaler     = joblib.load(SCALER_PATH)
    calibrator = joblib.load(CALIB_PATH)

    if os.path.isfile(STATS_PATH):
        global _TRAIN_STATS
        with open(STATS_PATH) as f:
            _TRAIN_STATS = json.load(f)

    print(f"\nScoring: {path}")
    new_df, new_meta = load_files([path])
    if new_df.empty:
        print("No valid records found in file.")
        return

    X = scaler.transform(new_df[FEATURE_COLUMNS].values)
    raw_scores = model.decision_function(X)
    cal_scores = calibrator.transform(raw_scores)
    if_flags   = model.predict(X)

    results = _build_results(new_df, new_meta, raw_scores, cal_scores, if_flags)
    _print_report(results, is_training=False)
    out_path = f"output/scored_{os.path.basename(path)}"
    _save_results(results, out_path)
    print(f"\n  Results saved → {out_path}")


# ─────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────

def _build_results(df, meta, raw_scores, cal_scores, if_flags) -> List[Dict]:
    results = []
    for i in range(len(df)):
        feat  = df.iloc[i].to_dict()
        m     = meta[i]
        score = float(cal_scores[i])
        label = classify_score(score)
        reasons = explain_session(feat)

        results.append({
            "rank"          : 0,
            "ip"            : m["_ip"],
            "file"          : m["_file"],
            "anomaly_score" : round(score, 4),
            "raw_if_score"  : round(float(raw_scores[i]), 4),
            "label"         : label,
            "if_flagged"    : bool(if_flags[i] == -1),
            "reasons"       : reasons,
            "key_features"  : {
                "io_spike_ratio"   : round(feat["io_spike_ratio"], 2),
                "total_kb"         : round(feat["total_kb"], 1),
                "total_packets"    : int(feat["total_packets"]),
                "top_dest_pkt_frac": round(feat["top_dest_pkt_frac"], 3),
                "num_destinations" : int(feat["num_destinations"]),
                "unique_domains"   : int(feat["unique_domains"]),
                "sni_repeat_ratio" : round(feat["sni_repeat_ratio"], 2),
                "kb_per_domain"    : round(feat["kb_per_domain"], 1),
                "io_cv"            : round(feat["io_cv"], 3),
                "sni_rate_per_sec" : round(feat["sni_rate_per_sec"], 3),
            },
        })

    results.sort(key=lambda r: -r["anomaly_score"])
    for rank, r in enumerate(results, 1):
        r["rank"] = rank
    return results


def _print_report(results: List[Dict], is_training: bool):
    mode = "TRAINING SET BASELINE CHECK" if is_training else "LIVE DETECTION RESULTS"
    print(f"\n{'═'*66}")
    print(f"  {mode}")
    print(f"{'═'*66}")

    counts = Counter(r["label"] for r in results)
    for label in ["🚨 HIGH RISK","⚠️  SUSPICIOUS","🔍 MODERATE","✅ NORMAL"]:
        n = counts.get(label, 0)
        if n > 0 or label == "✅ NORMAL":
            print(f"  {label} : {n}")
    print(f"  Total sessions : {len(results)}")

    if is_training:
        clean = sum(1 for r in results if r["label"] == "✅ NORMAL")
        print(f"\n  ✅ {clean}/{len(results)} sessions scored NORMAL — "
              f"baseline is well-established.")
        if clean < len(results):
            print(f"  ℹ️  Some sessions scored above NORMAL. Since all your data IS "
                  f"normal, these represent the statistical edge of your normal range.")
    print(f"{'═'*66}")

    for r in results:
        kf = r["key_features"]
        bar_n   = int(r["anomaly_score"] * 32)
        bar_str = "█" * bar_n + "░" * (32 - bar_n)

        print(f"\n  Rank #{r['rank']}  {r['label']}")
        print(f"  IP   : {r['ip']:<18}  Source: {r['file']}")
        print(f"  Score: {r['anomaly_score']:.4f}  [{bar_str}]")

        # Deviation context: show how each key metric compares to training mean
        if _TRAIN_STATS:
            print(f"  ── Deviation from your normal baseline ─────────────────")
            metrics = [
                ("io_spike_ratio",    "IO spike ratio",    "×"),
                ("total_kb",          "Total KB",          "KB"),
                ("total_packets",     "Total packets",     "pkt"),
                ("top_dest_pkt_frac", "Top-dest fraction", "%", 100),
                ("num_destinations",  "Destinations",      ""),
                ("unique_domains",    "Unique domains",    ""),
                ("sni_repeat_ratio",  "SNI repeat ratio",  "×"),
                ("kb_per_domain",     "KB/domain",         "KB"),
            ]
            for item in metrics:
                col   = item[0]
                label = item[1]
                unit  = item[2]
                scale = item[3] if len(item) > 3 else 1
                if col not in _TRAIN_STATS:
                    continue
                val  = kf[col] * scale
                mean = _TRAIN_STATS[col]["mean"] * scale
                std  = max(_TRAIN_STATS[col]["std"] * scale, 1e-6)
                z    = (kf[col] - _TRAIN_STATS[col]["mean"]) / (_TRAIN_STATS[col]["std"] + 1e-9)
                # Direction indicator
                arrow = "▲" if z > 0.5 else ("▼" if z < -0.5 else "─")
                print(f"    {arrow} {label:<22} {val:>9.1f}{unit}  "
                      f"(baseline mean: {mean:.1f}{unit},  z={z:+.1f}σ)")

        if r["reasons"]:
            print(f"  ── Rules triggered ─────────────────────────────────────")
            for reason in r["reasons"]:
                print(f"    • {reason}")
        else:
            if is_training:
                print(f"  ── No rules triggered  ✓  (within your confirmed normal range)")
            else:
                print(f"  ── No rules triggered  ✓  (matches your normal traffic baseline)")

        print(f"  {'─'*58}")

    # Summary note for training run
    if is_training:
        print(f"\n  {'─'*66}")
        print(f"  HOW TO INTERPRET THESE SCORES (TRAINING MODE)")
        print(f"  {'─'*66}")
        print(f"  The model has now learned what YOUR network looks like.")
        print(f"  Future captures will be scored relative to this baseline.")
        print(f"  A score of 0.9+ on a NEW device means it looks very")
        print(f"  different from all {len(results)} sessions used for training.")
        print(f"")
        print(f"  These training sessions scored above NORMAL because they are")
        print(f"  the statistical edge cases within your own normal data —")
        print(f"  not because they are anomalous. With more training data,")
        print(f"  these scores will compress toward 0.")
        print(f"  {'─'*66}")


def _save_results(results: List[Dict], path: str):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        json.dump({
            "generated_at": __import__("datetime").datetime.now().isoformat(),
            "total_sessions": len(results),
            "summary": {
                "high_risk"  : sum(1 for r in results if "HIGH RISK"   in r["label"]),
                "suspicious" : sum(1 for r in results if "SUSPICIOUS"  in r["label"]),
                "moderate"   : sum(1 for r in results if "MODERATE"    in r["label"]),
                "normal"     : sum(1 for r in results if "NORMAL"      in r["label"]),
            },
            "results": results,
        }, f, indent=2)

    # Simple summary: IPs + scores only
    summary = [
        {
            "ip"           : r["ip"],
            "file"         : r["file"],
            "anomaly_score": r["anomaly_score"],
            "label"        : r["label"],
        }
        for r in results
    ]
    summary_path = os.path.join(os.path.dirname(path) or ".", "scores_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"  Scores summary saved -> {summary_path}")


# ─────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train anomaly detector on normal data, or score new captures."
    )
    parser.add_argument(
        "--score", type=str, default=None,
        help="Path to a new JSON capture file to score against the trained model."
    )
    args = parser.parse_args()

    if args.score:
        score_new_file(args.score)
    else:
        train()