# CodeAlpha_BasicNetworkSniffer

## Overview

This project was completed as part of the CodeAlpha Cyber Security Internship.

The Basic Network Sniffer is developed in Python using the Scapy library. It captures live network packets and displays important packet information for educational and cybersecurity learning purposes.

## Features

- Capture live network packets
- Display Source IP Address
- Display Destination IP Address
- Identify Protocol (TCP, UDP, ICMP)
- Display Packet Length
- Display Timestamp
- Real-time Packet Monitoring

## Technologies Used

- Python 3.14
- Scapy
- Npcap
- VS Code

## Requirements

Install Scapy:

```bash
pip install scapy
```

Install Npcap on Windows before running the application.

## How to Run

```bash
python network_sniffer.py
```

Stop packet capture by pressing **Ctrl + C**.

## Sample Output

```
Packet #27
======================================================================
Timestamp        : 2026-07-07 13:11:40
Source IP        : 172.64.155.209
Destination IP   : 192.168.100.3
Protocol         : TCP
Source Port      : 443
Destination Port : 54193
Packet Length    : 322 bytes

```

## Learning Outcomes

- Network Packet Analysis
- IP Packet Inspection
- Protocol Identification
- Python Networking
- Cybersecurity Monitoring Basics

## Internship

CodeAlpha Cyber Security Internship

## Author

Abdul Wasay
