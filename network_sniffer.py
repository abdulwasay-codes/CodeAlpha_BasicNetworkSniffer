from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime

packet_count = 0


def process_packet(packet):
    global packet_count
    packet_count += 1

    print("\n" + "=" * 70)
    print(f"Packet #{packet_count}")
    print("=" * 70)

    print("Timestamp        :", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if IP in packet:
        print("Source IP        :", packet[IP].src)
        print("Destination IP   :", packet[IP].dst)

        if TCP in packet:
            print("Protocol         : TCP")
            print("Source Port      :", packet[TCP].sport)
            print("Destination Port :", packet[TCP].dport)

        elif UDP in packet:
            print("Protocol         : UDP")
            print("Source Port      :", packet[UDP].sport)
            print("Destination Port :", packet[UDP].dport)

        elif ICMP in packet:
            print("Protocol         : ICMP")

        else:
            print("Protocol         : Other")

    else:
        print("Protocol         : Non-IP Packet")

    print("Packet Length    :", len(packet), "bytes")


print("=" * 70)
print("        CodeAlpha Cyber Security Internship")
print("             Basic Network Sniffer")
print("=" * 70)
print("Capturing live network packets...")
print("Press Ctrl + C to stop.\n")

try:
    sniff(prn=process_packet, store=False)

except KeyboardInterrupt:
    print("\n\nPacket capture stopped successfully.")
    print(f"Total Packets Captured: {packet_count}")
    print("Thank you for using the Basic Network Sniffer!")