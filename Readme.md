# 🔐 Smart Network Gateway (CLI-Based Anomaly Detection)

A lightweight CLI-based smart gateway system that monitors network traffic, detects suspicious devices, and flags anomalies automatically using network scanning and traffic analysis.

---

## 🚀 Overview

This project acts as an **intelligent network gateway** that:

* Scans devices connected to a local network
* Analyzes traffic behavior using packet inspection
* Detects anomalies such as unusual traffic, unknown devices, or potential sniffers
* Prepares structured data for Machine Learning-based detection

---

## 🧠 Features

* 🔍 Network discovery using ARP and active scanning
* 📡 Traffic monitoring and analysis
* ⚠️ Suspicious device detection (rule-based + ML-ready)
* 🧾 JSON logging for all devices
* 🖥️ Fully CLI-based (lightweight & fast)

---

## 🛠️ Tech Stack

* **Python** – Core scripting & data processing
* **Nmap** – Network scanning & device analysis
* **TShark** – Packet capture & traffic insights
* **Kali Linux** – Testing environment

---

## 📂 Project Structure

```
smart-gateway/
│── scanner.py          # Runs Nmap scans
│── sniffer.py          # Captures traffic using TShark
│── parser.py           # Extracts features from raw data
│── model.py            # ML model / anomaly detection logic
│── network_data.json   # Raw collected data
│── dataset.csv         # Clean ML-ready dataset
│── main.py             # Entry point
```

---

## ⚙️ How It Works

```
Network Devices
      ↓
Nmap Scan + TShark Capture
      ↓
Raw JSON Data
      ↓
Feature Extraction
      ↓
ML Model / Rule Engine
      ↓
Anomaly Detection
```

---

## 🔍 Detection Logic

The system identifies suspicious behavior using:

* Unknown MAC vendors
* High number of external connections
* Unusual traffic volume
* Repeated rapid requests
* Promiscuous mode detection (with filtering to avoid false positives)

---

## 📊 Sample Features Used

| Feature          | Description              |
| ---------------- | ------------------------ |
| `open_ports`     | Number of open ports     |
| `latency`        | Device response time     |
| `connections`    | Total active connections |
| `unique_domains` | Domains accessed         |
| `data_kb`        | Data transferred         |
| `vendor_unknown` | Unknown MAC vendor flag  |

---

## 🧪 Example Output

```json
{
  "ip": "192.168.137.241",
  "connections": 5,
  "unique_domains": 3,
  "data_kb": 52,
  "vendor_unknown": 1,
  "anomaly_score": 0.72
}
```

---

## ⚠️ Important Notes

* Promiscuous mode detection may produce **false positives** on:

  * Gateways
  * Virtual machines
  * Hotspot networks

* The system uses **behavior-based detection**, not just port scanning

---

## 🔮 Future Improvements

* Real-time monitoring dashboard
* Automatic device blocking
* Advanced ML models (Isolation Forest, Autoencoders)
* Historical behavior tracking
* Alert system (email / notifications)

---

## 🧑‍💻 Usage

```bash
# Run full pipeline
python main.py
```

---

## 📌 Goal

To build a **self-learning smart gateway** that reduces manual network monitoring and improves security through automation.

---

## ⭐ Contributing

Feel free to fork and improve the project!

---

## 📜 License

MIT License
