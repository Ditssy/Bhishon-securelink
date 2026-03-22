import subprocess
import time

V3_SCRIPT = "v3script.py"
FLAG_SCRIPT = "flag.py"

DELAY = 20

while True:
    print("\n[+] Running network scan (v3script)...")
    subprocess.run(["python3", V3_SCRIPT])

    print("[+] Running threat detection (flag.py)...")
    subprocess.run(["python3", FLAG_SCRIPT])

    print(f"[+] Cycle complete. Waiting {DELAY} seconds...\n")
    time.sleep(DELAY)  # This was missing in the original — DELAY was defined but never used
