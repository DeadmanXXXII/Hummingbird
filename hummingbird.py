#!/usr/bin/env python3
import argparse
from modules.recon import recon
from modules.exploit_adb import exploit_adb
from modules.payload_dropper import deploy_payload
from modules.fingerprint import fingerprint
from utils.terminal_output import print_green, print_red, print_yellow, print_brew_style
from utils.install import install_dependencies

def banner():
    print(r"""
    ╔════════════════════════════════════════╗
    ║        hummingbird — Parrot Sec CLI    ║
    ║        Offensive tools for Android     ║
    ╚════════════════════════════════════════╝
    """)

def main():
    banner()
    parser = argparse.ArgumentParser(description="hummingbird - Android penetration testing tools")
    subparsers = parser.add_subparsers(dest="command")

    recon_parser = subparsers.add_parser("recon", help="Run Android recon")
    recon_parser.add_argument("--target", required=True)

    exploit_parser = subparsers.add_parser("exploit-adb", help="Attempt ADB RCE")
    exploit_parser.add_argument("--target", required=True)

    payload_parser = subparsers.add_parser("payload-dropper", help="Deploy Android payload")
    payload_parser.add_argument("--target", required=True)

    fp_parser = subparsers.add_parser("fingerprint", help="Fingerprint an Android system")
    fp_parser.add_argument("--target", required=True)

    install_parser = subparsers.add_parser("install", help="Install dependencies")

    args = parser.parse_args()

    if args.command == "recon":
        recon(args.target)
    elif args.command == "exploit-adb":
        exploit_adb(args.target)
    elif args.command == "payload-dropper":
        deploy_payload(args.target)
    elif args.command == "fingerprint":
        fingerprint(args.target)
    elif args.command == "install":
        install_dependencies()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()