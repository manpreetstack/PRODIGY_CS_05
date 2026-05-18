from scapy.all import sniff
from scapy.layers.inet import IP


def packet_callback(packet):
    if packet.haslayer(IP):
        print("\n=== Packet Captured ===")

        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
        print("Protocol:", packet[IP].proto)

        if packet.payload:
            print("Payload Data:")
            print(packet.payload)


print("=== Network Packet Analyzer ===")
print("Capturing packets... Press CTRL + C to stop.\n")

sniff(prn=packet_callback, store=False)