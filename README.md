# Packet Replay Script

This Python script allows you to replay network traffic captured in a `.pcap` file to a specified target IP address. It can be used for various legitimate network testing purposes, including troubleshooting, packet analysis, or network behavior testing on devices you own or have explicit permission to test.

**Important**: This script should only be used for **ethical testing** purposes on systems you own or have permission to test. Unauthorized packet replay or network traffic manipulation can lead to legal consequences and damage to network systems.

## Features
- Reads a `.pcap` file containing captured network packets.
- Sends the captured packets to a specified target IP address.
- Allows you to specify how many times to replay the packets or run it indefinitely.
- Supports adjusting the rate of packet sending by modifying the delay between each packet.

## Requirements
- Python 3.x
- [Scapy](https://scapy.readthedocs.io/en/latest/) library for packet manipulation and sending.


