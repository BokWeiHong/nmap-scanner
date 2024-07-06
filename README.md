## Nmap Automation Tool (Python)

This repository contains a Python script that automates basic network scanning using the `nmap` library.

**What is Nmap?**

Nmap (Network Mapper) is a free and open-source tool for network discovery and security auditing. It allows you to scan hosts and networks to identify open ports, services running on those ports, and the operating system of the target device.

**Using this Script**

This script provides a simple way to perform various Nmap scans on a targeted IP address.

**Requirements:**

- Python 3 (with `nmap` library installed: `pip install nmap`)

**Running the Script**

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the script: `python3 nmap_scanner.py` (replace `nmap_scanner.py` with the actual filename if different)
4. Follow the on-screen prompts:
   - Enter the IP address you want to scan.
   - Choose the type of scan you want to run (SYN ACK, UDP, or Comprehensive).

**Scan Types:**

- **SYN ACK Scan (TCP):** This is a common scan type that checks for open TCP ports by sending a SYN packet and analyzing the response.
- **UDP Scan:** This scan checks for open UDP ports, which are used by some network services.
- **Comprehensive Scan:** This performs a more extensive scan, including service version detection, service detection, script scanning, and operating system detection.

**Output:**

The script will display various information about the scan results, including:

- Nmap version
- Scan information (e.g., timing)
- IP status (up/down)
- Discovered protocols
- Open ports

**Important Note**

- Using Nmap for scanning requires permission from the network owner. It's crucial to respect network security practices and avoid unauthorized scanning.

**Disclaimer**

This script is provided for educational purposes only. The authors are not responsible for any misuse of this tool.
