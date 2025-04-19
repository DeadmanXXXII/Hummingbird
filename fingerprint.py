import os
from utils.terminal_output import print_green, print_red

def fingerprint(target):
    print(f"[+] Fingerprinting {target} as Android...")
    # Check for Android user agent or other identification mechanisms
    result = os.system(f"curl -s -I http://{target} | grep -i 'android'")
    if result == 0:
        print_green(f"[+] Android detected on {target}")
    else:
        print_red(f"[-] Not an Android device at {target}")