import scapy.all as scapy

arp_request_packet = scapy.ARP(pdst="192.168.32.1/24")
broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
combined_packet = broadcast_packet/arp_request_packet
answered, unanswered = scapy.srp(combined_packet, timeout=2, verbose=False)

for sent, received in answered:
    print(f"IP: {received.psrc}, MAC: {received.hwsrc}")
