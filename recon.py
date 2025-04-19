import os
from utils.terminal_output import print_green, print_red

def recon(target):
    print(f"[+] Performing Android recon on {target}...")
    # Example: Using tools like nmap or other Android recon tools
    result = os.system(f"nmap -p 5555 {target} -oG - | grep open")
    if result == 0:
        print_green(f"[+] Open port found on {target}")
    else:
        print_red(f"[-] No open ports found on {target}")