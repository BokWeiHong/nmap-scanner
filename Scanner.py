#!/usr/bin/python3

import nmap  # Import the nmap library for network scanning

scanner = nmap.PortScanner()  # Create a PortScanner object

print("Welcome, this is a simple nmap automation tool")
print("<-------------------------------------------->")

# Get the IP address to scan from the user
ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)

# Confirm the data type of the input (useful for debugging)
print(type(ip_addr))  # Should be <class 'str'>

# Prompt the user for the scan type with options
resp = input("""\nPlease enter the type of scan you want to run:
                1) SYN ACK scan (TCP ports)
                2) UDP scan (useful for some network services)
                3) Comprehensive Scan (extensive information gathering)
                Enter here: """)

print("You have selected option: ", resp)

if resp == '1':
    # Print Nmap version for reference
    print("Nmap Version: ", scanner.nmap_version())

    # Perform a SYN ACK scan (TCP) on ports 1-1023 with verbosity and stealth flags
    scanner.scan(ip_addr, '1-1023', '-v -sS')

    # Print scan information for debugging or logging
    print(scanner.scaninfo())

    # Get the IP status (e.g., up/down)
    print("IP Status: ", scanner[ip_addr].state())

    # Get all protocols discovered on the target IP
    print(scanner[ip_addr].all_protocols())

    # Print open TCP ports (keys of the 'tcp' dictionary)
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    # Similar logic for UDP scan, replace '-sS' with '-sU' for UDP
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1023', '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    # Perform a comprehensive scan with various flags
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1023', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp >= '4':
    print("Please enter a valid option (1, 2, or 3)")
