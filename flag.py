import json
import re
import smtplib
from email.message import EmailMessage

# Load the JSON data
with open('network_data.json', 'r') as f:
    data = json.load(f)

# Initialize our lists
ip_addresses = []
mac_addresses = []
sniffer_results = []
io_averages = []

for ip, details in data.items():
    # 1. Store IP Address
    ip_addresses.append(ip)
    
    # 2. Extract MAC Address from the Nmap string
    # Pattern looks for 'MAC Address: ' followed by hex pairs
    mac_match = re.search(r"MAC Address: ([0-9A-F:]+)", details['nmap'])
    mac_addresses.append(mac_match.group(1) if mac_match else "Unknown")
    
    # 3. Extract Sniffer-detect result from the Nmap string
    # Pattern looks for the line starting with |_sniffer-detect:
    sniffer_match = re.search(r"sniffer-detect: (.*?)\s*\(tests:", details['nmap'])
    sniffer_results.append(sniffer_match.group(1).strip() if sniffer_match else "Not Found")
    
    # 4. Calculate Average of io_stats
    stats = details.get('io_stats', [])
    if stats:
        avg = sum(stats) / len(stats)
        io_averages.append(round(avg, 2))
    else:
        io_averages.append(0.0)

def flagScript(ip_addresses, mac_addresses, sniffer_results, io_averages):
    body = []

    # TRACKING FOR DUPLICATES
    # Count occurrences of each IP and MAC
    ip_counts = {ip: ip_addresses.count(ip) for ip in set(ip_addresses)}
    mac_counts = {mac: mac_addresses.count(mac) for mac in set(mac_addresses)}

    for i in range(len(ip_addresses)):
        current_ip = ip_addresses[i]
        current_mac = mac_addresses[i]

        # 1. FOR PROMISCUOUS MODE
        if sniffer_results[i] != "Unknown":
            if 10000 < io_averages[i] <= 12000:
                body.append(f"***Alert*** Promiscuous Alert: IP {current_ip} (MAC: {current_mac}) (Highest Packets per sec: {io_averages[i]} )")
            
        # 2. FOR PPS BURST
        if io_averages[i] > 12000:
            body.append(f"PPS Burst detected at {current_ip} (Highest Packets per sec: {io_averages[i]} )")

        # 3. FOR DUPLICATES
        if ip_counts[current_ip] > 1:
            body.append(f"Duplicate IP Found: {current_ip}")
        
        if mac_counts[current_mac] > 1:
            body.append(f"Duplicate MAC Found: {current_mac}")

    return set(body)

def send_frame_report(body, receiver_email):
    # Setup your credentials
    sender_email = "pritishmondal05.pro@gmail.com"
    app_password = "nzjs shse ytgp xztx"  # 16-character App Password

    # Create the email content
    msg = EmailMessage()
    msg['Subject'] = "Smart GateWay Security Risk (Admin Approval)"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    # Format the frame list into a readable string
    msg.set_content(body)

    # Send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

data = flagScript(ip_addresses, mac_addresses, sniffer_results, io_averages)

if data:
    for i in data:
        send_frame_report(i, "krak3n.oceanus@gmail.com")
else:
    print("Secured")
