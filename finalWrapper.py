import subprocess
import time

V3_SCRIPT = "v3script.py"
FLAG_SCRIPT = "flag.py"

DELAY = 5

while True:
    print("\n[+] Running network scan (v3script)...")
    
    subprocess.run(["python3", V3_SCRIPT])

    print("[+] Running threat detection (flag.py)...")
    
    subprocess.run(["python3", FLAG_SCRIPT])

    print(f"[+] Cycle complete. Waiting {DELAY} seconds...\n")
