<div align="center">

```
███████╗███╗   ███╗ █████╗ ██████╗ ████████╗     ██████╗  █████╗ ████████╗███████╗██╗    ██╗ █████╗ ██╗   ██╗
██╔════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝    ██╔════╝ ██╔══██╗╚══██╔══╝██╔════╝██║    ██║██╔══██╗╚██╗ ██╔╝
███████╗██╔████╔██║███████║██████╔╝   ██║       ██║  ███╗███████║   ██║   █████╗  ██║ █╗ ██║███████║ ╚████╔╝
╚════██║██║╚██╔╝██║██╔══██║██╔══██╗   ██║       ██║   ██║██╔══██║   ██║   ██╔══╝  ██║███╗██║██╔══██║  ╚██╔╝
███████║██║ ╚═╝ ██║██║  ██║██║  ██║   ██║       ╚██████╔╝██║  ██║   ██║   ███████╗╚███╔███╔╝██║  ██║   ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝
```

### 🔐 Your network's silent guardian. Always watching. Never sleeping.

![Saffron](https://img.shields.io/badge/🟧-Saffron-FF9933?style=flat-square&color=FF9933)
![White](https://img.shields.io/badge/⬜-White-ffffff?style=flat-square&color=ffffff&labelColor=ffffff)
![Green](https://img.shields.io/badge/🟩-Green-138808?style=flat-square&color=138808)
![Chakra](https://img.shields.io/badge/☸-Ashoka_Chakra-000080?style=flat-square&color=000080)

[![Python](https://img.shields.io/badge/Python-3.8+-FF9933?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Nmap](https://img.shields.io/badge/Nmap-Scanner-138808?style=for-the-badge&logoColor=white)](https://nmap.org)
[![TShark](https://img.shields.io/badge/TShark-Packet_Analysis-000080?style=for-the-badge&logo=wireshark&logoColor=white)](https://wireshark.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Isolation_Forest-FF9933?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-138808?style=for-the-badge)](LICENSE)

> AI-powered, real-time network defense — detects threats, blocks attackers, alerts admins.
> **Automatically. Instantly. No human required.**

━━━ 🟧 ━━━━━━━━━━━━━━━━━━━━ ☸ ━━━━━━━━━━━━━━━━━━━━ 🟩 ━━━

</div>

---

## 🧠 The Story

Most network security tools are glorified loggers. They see everything. They understand nothing.

Nmap tells you what's on your network. Wireshark shows you every packet. But neither of them will stop the hacked IoT device that started flooding your network at 2am. Neither will notice the device quietly running in promiscuous mode, reading everyone's traffic. Neither will catch the MAC spoofer pretending to be your trusted server.

**Smart Gateway does.**

It watches your network the way a security analyst would — learning what normal looks like, spotting when something breaks that pattern, and acting before you even open your laptop.

---

## ⚡ What Happens When a Threat Is Detected

```
Device acts suspiciously
        │
        ▼
┌─────────────────────┐
│  ML scores anomaly  │  ← Isolation Forest compares against learned baseline
└────────┬────────────┘
         │  THREAT CONFIRMED
         ▼
┌────────────────────────────────────────┐
│  1. Device is BLOCKED from network     │
│  2. Admin receives EMAIL ALERT         │
│  3. Anomaly is LOGGED for analysis     │
└────────────────────────────────────────┘
         │
         ▼
    You sleep peacefully.
```

---

## 🚨 Threats It Catches

| Attack | Signal | How Smart Gateway Catches It |
|--------|--------|-------------------------------|
| Hacked IoT flooding network | 📈 Traffic spike | PPS shoots past adaptive threshold → flagged |
| Packet sniffing / MITM setup | 👁️ Promiscuous mode | Interface flag detected → cross-checked with traffic |
| MAC/IP spoofing | 🔀 Address mismatch | IP-MAC consistency verified over time → flagged |
| Rogue device joins network | 🏷️ Unknown vendor / duplicate MAC | Device integrity check fails → flagged |

---

## 📊 System Flowcharts

### 1 — Overall System Flow

```
 ┌──────────────────┐                        ┌──────────────────┐
 │   Nmap scanner   │                        │  TShark capture  │
 │  Device discovery│                        │ Live traffic data│
 └────────┬─────────┘                        └────────┬─────────┘
          │                                           │
          └─────────────────┬─────────────────────────┘
                            │
                            ▼
                   ┌──────────────────┐
                   │Feature engineering│
                   │ JSON → ML features│
                   └────────┬─────────┘
                            │
                            ▼
                   ┌──────────────────┐
                   │  Isolation Forest │
                   │  Anomaly scoring  │
                   └────────┬─────────┘
                            │
                ┌───────────▼────────────┐
                │    Threat detected?    │
                └───────────────────────┘
                      │           │
                     YES          NO
                      │           │
                      ▼           ▼
           ┌───────────────┐  ┌──────────────┐
           │ Response      │  │  Continue    │
           │ engine fires  │  │  monitoring  │
           └───────┬───────┘  └──────────────┘
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
 ┌──────────┐ ┌──────────┐ ┌──────────┐
 │  Block   │ │  Email   │ │   Log    │
 │  device  │ │  alert   │ │ anomaly  │
 └──────────┘ └──────────┘ └──────────┘
```

---

### 2 — Multi-Signal Threat Detection

```
                   ┌──────────────────────┐
                   │    Device observed   │
                   └──────────┬───────────┘
                              │
          ┌───────────────────┼───────────────────┐───────────────────┐
          │                   │                   │                   │
          ▼                   ▼                   ▼                   ▼
  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
  │  PPS spike?  │   │  Promisc     │   │  IP–MAC      │   │  Bad device  │
  │  vs baseline │   │  mode?       │   │  mismatch?   │   │  integrity?  │
  └──────┬───────┘   └──────┬───────┘   └──────┬───────┘   └──────┬───────┘
         │                  │                  │                  │
    +1 signal          +1 signal          +1 signal          +1 signal
         │                  │                  │                  │
         └──────────────────┴──────────────────┴──────────────────┘
                                      │
                                      ▼
                         ┌────────────────────────┐
                         │   Signal aggregator    │
                         │   Count indicators     │
                         └────────────┬───────────┘
                                      │
                         ┌────────────▼───────────┐
                         │     Signals ≥ 2 ?      │
                         └────────────────────────┘
                               │            │
                              YES            NO
                               │            │
                               ▼            ▼
                    ┌──────────────────┐  ┌────────┐
                    │  Isolation Forest│  │  Clear │
                    │  confirms        │  └────────┘
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Response engine │
                    └──────────────────┘
```

---

### 3 — Automated Response Engine

```
          ┌───────────────────────────────────┐
          │          Threat confirmed          │
          │       Score exceeds threshold      │
          └──────────────────┬────────────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
       ┌────────────┐ ┌────────────┐ ┌────────────┐
       │   BLOCK    │ │   EMAIL    │ │    LOG     │
       │            │ │   ALERT    │ │   ANOMALY  │
       │ Isolate    │ │ Device +   │ │ Timestamp  │
       │ from net   │ │ threat     │ │ + signals  │
       │ instantly  │ │ details    │ │ + score    │
       └────────────┘ └────────────┘ └────────────┘
              │              │              │
              └──────────────┴──────────────┘
                             │
                             ▼
          ┌───────────────────────────────────┐
          │          Resume monitoring         │
          │   System keeps watching network    │
          └───────────────────────────────────┘
```

---

### 4 — Data Pipeline

```
  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
  │  Raw     │    │  JSON    │    │ Feature  │    │   Iso    │    │Decision  │
  │ packets  │───▶│  parser  │───▶│  eng.    │───▶│  Forest  │───▶│threat /  │
  │          │    │          │    │ PPS,     │    │ scores   │    │  clear   │
  │ TShark   │    │ per-dev  │    │ promisc  │    │ vs.      │    │          │
  │ stream   │    │ record   │    │ IP-MAC   │    │ baseline │    │          │
  └──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
```

---

### 5 — False Positive Prevention

```
                   ┌──────────────────────┐
                   │    Signal detected   │
                   └──────────┬───────────┘
                              │
                              ▼
         ┌────────────────────────────────────────┐
         │  Check 1 — PPS spike                   │──── within normal ────▶ PASS
         │  vs. rolling average, not fixed cutoff │
         └─────────────────────┬──────────────────┘
                               │  spike confirmed
                               ▼
         ┌────────────────────────────────────────┐
         │  Check 2 — Promiscuous mode            │──── mode only, ────────▶ PASS
         │  only flag if traffic anomaly present  │      no traffic anomaly
         └─────────────────────┬──────────────────┘
                               │  both confirmed
                               ▼
         ┌────────────────────────────────────────┐
         │  Check 3 — IP–MAC mismatch             │──── single scan ───────▶ PASS
         │  persistent over multiple scans        │      occurrence only
         └─────────────────────┬──────────────────┘
                               │  persistent confirmed
                               ▼
         ┌────────────────────────────────────────┐
         │  Multi-signal gate                     │
         │  ≥ 2 checks triggered → threat flagged │
         └─────────────────────┬──────────────────┘
                               │
                               ▼
                   ┌──────────────────────┐
                   │    Response engine   │
                   └──────────────────────┘
```

---

## 🧰 Tools & Technologies

| Category | Tool | Purpose |
|----------|------|---------|
| 🔍 Network scanning | **Nmap** | Discovers all devices — IP, MAC, vendor, open ports |
| 📦 Packet capture | **TShark** | CLI Wireshark; captures live traffic per device |
| 🐍 Backend | **Python 3.8+** | Core orchestration, signal processing, response logic |
| 🤖 ML Model | **Isolation Forest** (scikit-learn) | Unsupervised anomaly detection vs. learned baseline |
| 🔧 Data pipeline | **JSON + Pandas** | Structures raw capture into ML-ready feature vectors |
| 📊 Feature engineering | **NumPy** | PPS calculation, rolling averages, delta tracking |
| 📧 Alerting | **SMTP (smtplib)** | Real-time email alerts to network admin |
| 🚫 Blocking | **iptables / netsh** | Auto-blocks flagged device at OS network layer |
| 🗂️ Logging | **Python logging** | Structured anomaly logs with timestamps and signal details |

---

## 🛠️ How We Built It

Nmap continuously maps every device. TShark captures live traffic and extracts per-device behavior — packets per second, protocol patterns, interface flags. Raw data flows into a feature engineering pipeline and gets scored by an Isolation Forest model trained on normal behavior. The moment a device breaks pattern — it gets blocked automatically, the admin gets an email alert, and everything gets logged. The whole thing runs in real time. No human in the loop required.

---

## 🚀 Getting Started

**Requirements**
```bash
Python 3.8+
Nmap
TShark (Wireshark CLI)
```

**Install**
```bash
git clone https://github.com/yourusername/smart-gateway.git
cd smart-gateway
pip install -r requirements.txt
```

**Configure email alerts**
```python
# config.py
SMTP_HOST     = "smtp.gmail.com"
SMTP_PORT     = 587
ALERT_EMAIL   = "admin@yourdomain.com"
SMTP_PASSWORD = "your_app_password"
```

**Run**
```bash
sudo python main.py
```
> ⚠️ Requires root/admin privileges for raw packet capture and device blocking.

---

## 📁 Project Structure

```
smart-gateway/
├── main.py                  # Entry point — starts all monitors
├── config.py                # Settings, thresholds, SMTP config
├── scanner/
│   ├── nmap_scanner.py      # Device discovery & continuous tracking
│   └── tshark_capture.py    # Live traffic capture & per-device metrics
├── detection/
│   ├── feature_eng.py       # JSON → ML-ready features (PPS, flags, deltas)
│   ├── model.py             # Isolation Forest training & anomaly scoring
│   └── signals.py           # PPS spike, promiscuous, IP-MAC, integrity checks
├── response/
│   ├── blocker.py           # Auto device blocking via iptables/netsh
│   └── alerter.py           # Email notification via SMTP
├── logs/                    # Timestamped anomaly records
└── requirements.txt
```

---

## 🎯 Why This Is Different

| Feature | Nmap | Wireshark | **Smart Gateway** |
|---------|:----:|:---------:|:-----------------:|
| Device discovery | ✅ | ❌ | ✅ |
| Live traffic capture | ❌ | ✅ | ✅ |
| Real-time analysis | ❌ | ❌ | ✅ |
| Behavior-based ML detection | ❌ | ❌ | ✅ |
| Auto blocking | ❌ | ❌ | ✅ |
| Admin email alerts | ❌ | ❌ | ✅ |
| Needs human to act | ✅ | ✅ | ❌ |

---

## 🔬 Detection Deep Dive

**Adaptive PPS Threshold** — rather than a fixed cutoff, the system maintains a rolling baseline per device. A spike has to be meaningfully above *that device's* normal — not some global number.

**Promiscuous Mode** — a strong MITM/sniffing indicator, but VMs and some adapters can false-positive. Smart Gateway uses it as a *supporting signal only* — it confirms, never accuses alone.

**IP–MAC Consistency** — spoofing attacks often recycle IPs with forged MACs. The system tracks mappings over time and flags persistent inconsistencies, not one-off DHCP quirks.

**Device Integrity** — unknown OUI vendor, duplicate MAC, or mismatched identity across scans? Any of these alone is suspicious. Multiple together triggers a block.

---

## 🧩 Challenges We Solved

**1. Real threats vs. normal traffic spikes** — Sudden PPS spikes also happen during legitimate usage. Solved with adaptive thresholds based on rolling average PPS. Multiple signals must align before any alert fires.

**2. Promiscuous mode false positives** — VMs and certain adapters trigger promiscuous mode without malicious intent. Made it a supporting signal only — confirmed alongside traffic anomalies before action.

**3. Accurate spoofing detection** — IP-MAC mismatches can be noisy in dynamic DHCP environments. Consistency verified over time, cross-referenced against network activity patterns before flagging.

---

## ⚠️ Disclaimer

Smart Gateway is built for **authorized network environments only**. Only deploy on networks you own or have explicit permission to monitor. Unauthorized network scanning and traffic analysis is illegal in most jurisdictions.

---

## 🤝 Contributing

PRs welcome. If you find a false positive pattern we haven't handled, open an issue — that's genuinely valuable data.

---

## 📄 License

MIT License — use it, build on it, just don't be evil with it.

---

<div align="center">

**Built at a hackathon. Designed to actually work.**

*We're not just detecting attacks — we're stopping them as they happen.*

━━━ 🟧 ━━━━━━━━━━━━━━━━━━━━ ☸ ━━━━━━━━━━━━━━━━━━━━ 🟩 ━━━

</div>
