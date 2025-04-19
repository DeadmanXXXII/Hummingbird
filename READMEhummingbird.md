# Hummingbird - Parrot Security OS-inspired Android CLI

Hummingbird is a CLI tool designed to simulate offensive security actions on Android systems, inspired by Parrot Security OS. It is a modular framework with tools for reconnaissance, ADB exploits, payload deployment, and fingerprinting Android systems.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hummingbird.git
   cd hummingbird
   ```

2. Install dependencies:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. Make hummingbird.py executable:
   ```bash
   chmod +x hummingbird.py
   ln -s $(pwd)/hummingbird.py /usr/local/bin/hummingbird
   ```

## Usage

- **Recon:**
  ```bash
  hummingbird recon --target <target-ip>
  ```

- **Exploit ADB:**
  ```bash
  hummingbird exploit-adb --target <target-ip>
  ```

- **Deploy Payload:**
  ```bash
  hummingbird payload-dropper --target <target-ip>
  ```

- **Fingerprint Android:**
  ```bash
  hummingbird fingerprint --target <target-ip>
  ```

- **Install dependencies:**
  ```bash
  hummingbird install
  ```

## Contributing

Feel free to fork, modify, and submit pull requests. This is a community-driven project.

## Disclaimer

This tool is for educational purposes only. Ensure you have permission before testing on any system.