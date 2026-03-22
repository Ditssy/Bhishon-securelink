import subprocess
import re
import json

INTERFACE = "eth1"
NETWORK = "192.168.137.0/24"
CAPTURE_TIME = 20


# -------------------------------
# Run shell command
# -------------------------------
def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout


# -------------------------------
# 1. ARP Scan → Active IPs
# -------------------------------
def get_active_ips():
    print("[+] Running ARP scan...")
    cmd = f"sudo arp-scan --interface={INTERFACE} {NETWORK}"
    output = run(cmd)

    ips = []
    for line in output.split("\n"):
        match = re.match(r"(\d+\.\d+\.\d+\.\d+)", line)
        if match:
            ips.append(match.group(1))

    return ips


# -------------------------------
# 2. Nmap Discovery
# -------------------------------
def nmap_discovery(ip):
    cmd = f"nmap --script=sniffer-detect {ip}"
    return run(cmd)


# -------------------------------
# 3. Tshark SNI
# -------------------------------
def tshark_sni(ip):
    cmd = f"""
    sudo tshark -i {INTERFACE} \
    -f "host {ip}" \
    -Y "tls.handshake.extensions_server_name" \
    -T fields \
    -e frame.time \
    -e ip.dst \
    -e tls.handshake.extensions_server_name \
    -a duration:{CAPTURE_TIME}
    """

    output = run(cmd)

    rows = []
    for line in output.strip().split("\n"):
        parts = line.split("\t")
        if len(parts) == 3:
            rows.append({
                "time": parts[0],
                "destination": parts[1],
                "domain": parts[2]
            })

    return rows


# -------------------------------
# 4. Tshark Conversations
# -------------------------------
def tshark_conv(ip):
    cmd = f"""
    tshark -i {INTERFACE} \
    -f "host {ip}" \
    -q \
    -z conv,ip \
    -a duration:{CAPTURE_TIME}
    """

    output = run(cmd)

    rows = []
    capture = False

    for line in output.split("\n"):
        if "IPv4 Conversations" in line:
            capture = True
            continue

        if capture:
            if line.strip() == "" or "===" in line:
                continue

            match = re.search(
                r"(\d+\.\d+\.\d+\.\d+)\s+<->\s+(\d+\.\d+\.\d+\.\d+).*?(\d+\s+[\d,]+\s*\wB)",
                line,
            )
            if match:
                src, dst, data = match.groups()
                rows.append({
                    "source": src,
                    "destination": dst,
                    "data": data
                })

    return rows


# -------------------------------
# 5. Tshark IO Stats (PPS)
# -------------------------------
def tshark_iostat(ip):
    cmd = f"""
    sudo tshark -i {INTERFACE} \
    -f "host {ip}" \
    -q \
    -z io,stat,1 \
    -a duration:{CAPTURE_TIME}
    """

    output = run(cmd)
    print(output)

    frames = []

    for line in output.strip().split('\n'):
        if '<>' in line:
            # All lines below must use consistent spaces (no tabs!)
            columns = line.split('|')
            if len(columns) >= 3:
                value = columns[2].strip()
                frames.append(int(value))

    return frames


# -------------------------------
# Pretty print table
# -------------------------------
def print_table(title, headers, rows):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)

    print(" | ".join(headers))
    print("-" * 80)

    for row in rows:
        print(" | ".join(str(row[h]) for h in headers))


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":

    all_data = {}

    ips = get_active_ips()
    print(f"\n[+] Active IPs: {ips}\n")

    for ip in ips:
        print("\n" + "#" * 80)
        print(f"[ DEVICE: {ip} ]")
        print("#" * 80)

        device_data = {}

        # --- Nmap ---
        print("[+] Running Nmap...")
        nmap_output = nmap_discovery(ip)
        device_data["nmap"] = nmap_output
        print(nmap_output)

        # --- SNI ---
        print("[+] Capturing SNI...")
        sni = tshark_sni(ip)
        device_data["sni"] = sni

        print_table(
            f"SNI Domains for {ip}",
            ["time", "destination", "domain"],
            sni
        )

        # --- Conversations ---
        print("[+] Capturing Conversations...")
        conv = tshark_conv(ip)
        device_data["conversations"] = conv

        print_table(
            f"Conversations for {ip}",
            ["source", "destination", "data"],
            conv
        )

        # --- IO Stats (PPS) ---
        print("[+] Capturing IO Stats...")
        io_stats = tshark_iostat(ip)
        device_data["io_stats"] = io_stats
        print(io_stats)

        all_data[ip] = device_data

    # -------------------------------
    # Save JSON
    # -------------------------------
    with open("network_data.json", "w") as f:
        json.dump(all_data, f, indent=4)

    print("\n[+] Data saved to network_data.json")
