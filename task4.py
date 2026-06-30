from scapy.all import rdpcap, IP

file = input("Enter PCAP file name: ")

packets = rdpcap(file)

print("\nNETWORK PACKET ANALYZER")
print("=" * 50)

for i, packet in enumerate(packets, start=1):

    if packet.haslayer(IP):
        print(f"\nPacket {i}")
        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)
        print("Protocol       :", packet[IP].proto)
        print("-" * 50)

print("\nAnalysis Completed")
from scapy.all import *

p1 = IP(src="192.168.1.10", dst="8.8.8.8")/TCP()/Raw(load="Hello")
p2 = IP(src="8.8.8.8", dst="192.168.1.10")/TCP()/Raw(load="Reply")
p3 = IP(src="192.168.1.10", dst="1.1.1.1")/UDP()/Raw(load="DNS Query")

wrpcap("data.pcap", [p1, p2, p3])

print("PCAP file created successfully!")
