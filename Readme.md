<div align="center">

```
███████╗███╗   ███╗ █████╗ ██████╗ ████████╗     ██████╗  █████╗ ████████╗███████╗██╗    ██╗ █████╗ ██╗   ██╗
██╔════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝    ██╔════╝ ██╔══██╗╚══██╔══╝██╔════╝██║    ██║██╔══██╗╚██╗ ██╔╝
███████╗██╔████╔██║███████║██████╔╝   ██║       ██║  ███╗███████║   ██║   █████╗  ██║ █╗ ██║███████║ ╚████╔╝ 
╚════██║██║╚██╔╝██║██╔══██║██╔══██╗   ██║       ██║   ██║██╔══██║   ██║   ██╔══╝  ██║███╗██║██╔══██║  ╚██╔╝  
███████║██║ ╚═╝ ██║██║  ██║██║  ██║   ██║       ╚██████╔╝██║  ██║   ██║   ███████╗╚███╔███╔╝██║  ██║   ██║   
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝  
```

# 🔐 Smart Network Gateway

### *Your network's silent guardian. Always watching. Never sleeping.*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Nmap](https://img.shields.io/badge/Nmap-7.x-0E83CD?style=for-the-badge&logo=nmap&logoColor=white)](https://nmap.org)
[![TShark](https://img.shields.io/badge/TShark-4.x-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)](https://wireshark.org)
[![Kali Linux](https://img.shields.io/badge/Kali_Linux-2024-268BEE?style=for-the-badge&logo=kalilinux&logoColor=white)](https://kali.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![ML Ready](https://img.shields.io/badge/ML--Ready-Isolation_Forest-f97316?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org)

</div>

---

## 🌐 What Is This?

> **Smart Gateway** is a CLI-first, Python-powered network intelligence tool that **watches your LAN like a hawk** — scanning every device, sniffing suspicious traffic, and surfacing threats before they escalate.

No bloated GUI. No unnecessary overhead. Just raw, terminal-grade **network awareness**.

```bash
$ python main.py

[*] Initializing Smart Gateway v1.0...
[*] Scanning 192.168.137.0/24 — found 14 devices
[!] ANOMALY DETECTED: 192.168.137.241 — score: 0.72
    ↳ Unknown MAC vendor | 5 active connections | Possible sniffer
[✓] Report saved → network_data.json
```

---

## ⚡ Feature Highlights

| Feature | Description |
|--------|-------------|
| 🔍 **ARP Discovery** | Instantly maps every device on your LAN |
| 📡 **Packet Inspection** | Deep traffic capture via TShark |
| 🧠 **Anomaly Engine** | Rule-based detection pipeline |
| 🧾 **JSON Logging** | Structured, queryable logs for every scan |
| 🚀 **CLI-First** | Lightweight — runs on anything, even a Pi |
| 🛡️ **Sniffer Detection** | Catches promiscuous mode devices |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      YOUR LOCAL NETWORK                         │
│   [Phone] [Laptop] [IoT] [???Unknown???] [Smart TV] [Router]   │
└──────────────────────────┬──────────────────────────────────────┘
                           │
              ┌────────────▼────────────┐
              │   Nmap + TShark Layer   │  ← Active scan + passive capture
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │   Raw JSON Data Store   │  ← network_data.json
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │   Feature Extraction    │  ← parser.py
              │  ports · latency ·      │
              │  domains · data_kb      │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │  ML Model / Rule Engine │  ← model.py
              │   Isolation Forest /    │
              │   Behavioral Rules      │
              └────────────┬────────────┘
                           │
              ┌────────────▼────────────┐
              │   🚨 ANOMALY REPORT 🚨  │
              └─────────────────────────┘
```

---

## 📂 Project Structure

```
smart-gateway/
│
├── 🐍 main.py              # Entry point — runs the full pipeline
├── 🔭 scanner.py           # Nmap-based network discovery & port scanning
├── 📡 sniffer.py           # TShark packet capture & traffic monitoring
├── ⚙️  parser.py           # Feature extraction from raw scan data
├── 🧠 model.py             # Anomaly detection (rules + ML-ready)
│
├── 📊 network_data.json    # Raw device & traffic data (auto-generated)
└── 📈 dataset.csv          # Clean, ML-ready feature dataset
```

---

## 🚀 Getting Started

### Prerequisites

```bash
# Install system dependencies
sudo apt update && sudo apt install -y nmap tshark

# Install Python dependencies
pip install -r requirements.txt
```

### Run It

```bash
# Full pipeline — scan, capture, detect
python main.py

# Optional: specify your network interface
python main.py --interface eth0

# Output logs to file
python main.py --output results.json
```

---

## 🧠 Detection Logic

The anomaly engine scores every device on a **0.0 → 1.0 risk scale** using:

```
Risk Score = weighted_sum(
    vendor_unknown      × 0.30   # Unknown MAC = red flag
    open_ports          × 0.20   # Excessive open ports
    unique_domains      × 0.20   # Unusually broad DNS activity
    connection_rate     × 0.15   # Rapid repeated requests
    promiscuous_mode    × 0.15   # Possible sniffer on network
)
```

**Score thresholds:**

| Score | Status | Action |
|-------|--------|--------|
| `0.0 – 0.35` | ✅ Clean | Normal device |
| `0.35 – 0.60` | ⚠️ Suspicious | Flag & monitor |
| `0.60 – 1.0` | 🚨 Anomaly | Alert + log |

---

## 📊 Sample Output

```json
{
  "timestamp": "2025-06-15T22:41:03Z",
  "ip": "192.168.137.241",
  "mac": "DE:AD:BE:EF:00:01",
  "vendor": "UNKNOWN",
  "open_ports": 11,
  "latency_ms": 3.2,
  "connections": 5,
  "unique_domains": 3,
  "data_kb": 52,
  "vendor_unknown": 1,
  "anomaly_score": 0.72,
  "verdict": "⚠️  SUSPICIOUS — possible rogue device"
}
```

---

## 📡 Feature Vector

| Feature | Type | Description |
|---------|------|-------------|
| `open_ports` | `int` | Number of open ports detected |
| `latency_ms` | `float` | Device ping response time |
| `connections` | `int` | Total active TCP/UDP connections |
| `unique_domains` | `int` | Distinct domains queried |
| `data_kb` | `float` | Data transferred in session |
| `vendor_unknown` | `bool` | MAC vendor not in known registry |

---

## ⚠️ Known Limitations

> Before you panic at your router — read this.

- **Gateways & Routers** often appear in promiscuous mode — this is normal
- **Virtual Machines** (VirtualBox, VMware) may trigger vendor-unknown flags
- **Mobile Hotspots** behave like mini-gateways and may score higher than expected
- This tool is **behavior-based**, not signature-based — think IDS, not antivirus

---

## 🔮 Roadmap

```
v1.0  ✅  Rule-based anomaly detection + JSON logging
v1.1  🔄  Isolation Forest + Autoencoder ML integration
v1.2  📅  Historical behavior tracking per device
v1.3  📅  Email/webhook alert system
v2.0  📅  Real-time web dashboard (FastAPI + HTMX)
v2.1  📅  Automatic device quarantine / firewall rules
```

---

## 🤝 Contributing

Found a bug? Have an idea? PRs are welcome.

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
# Open a Pull Request ✨
```

---

## 📜 License

```
MIT License — use it, fork it, break it, improve it.
Just don't sniff traffic you don't own. 🙂
```

---

<div align="center">

**Built for security nerds. Runs on caffeine and curiosity.**

*If this helped you, drop a ⭐ — it means a lot.*

</div>
