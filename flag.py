import json
import re
import smtplib
from email.message import EmailMessage
import subprocess

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout
    
    
def send_frame_report(ip,score, receiver_email):
    sender_email = "sender@gmail.com"
    app_password = "xxxx xxxx xxxx xxxx"  # 16-character App Password

    msg = EmailMessage()
    msg['Subject'] = "Security Risk (Admin Approval)"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(f"The Device {ip} on your network is acting suspicious with a score of {score}.")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
        
def send_frame_report_blocked(ip,score, receiver_email):
    sender_email = "sender@gmail.com"
    app_password = "xxxx xxxx xxxx xxxx"  # 16-character App Password

    msg = EmailMessage()
    msg['Subject'] = "Security Risk (Action Taken)"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(f"The Device {ip} on your network was acting suspicious with a score of {score}. ACTION TAKEN -> Device Blocked")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

    

cmd = f"python3 train_and_score.py --score network_data.json"
run(cmd)

with open('output/scores_summary.json', 'r') as f:
    data = json.load(f)
    
for item in data:
    ip = item["ip"]
    score = item["anomaly_score"]
    if score>=0.6 and score<=0.85:
        send_frame_report(ip,score, "receiver@gmail.com")
    elif score>0.85:
        cmd1 = f"sudo iptables -I FORWARD 1 -i wlx002e2d002e28 -s {ip} -j DROP"
        cmd2 = f"sudo iptables -I FORWARD 1 -d {ip} -j DROP"
        run(cmd1)
        run(cmd2)
        send_frame_report_blocked(ip,score, "receiver@gmail.com")
    else:
        print("Secured")
        

