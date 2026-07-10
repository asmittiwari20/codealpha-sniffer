from scapy.all import sniff, IP, conf

# Force Scapy to use standard Layer 3 sockets instead of Layer 2
conf.L3socket = conf.L3socket6 

def process_packet(packet):
    if packet.haslayer(IP):
        print(f"Source: {packet[IP].src} --> Dest: {packet[IP].dst}")

print("Sniffer is running... Press Ctrl+C to stop.")
sniff(prn=process_packet, count=10)