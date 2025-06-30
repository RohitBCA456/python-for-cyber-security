import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast/arp_request

    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    client_List = []

    for element in answered:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_List.append(client_dict) 
    return client_List

def print_result(scan_result):
    print("IP\t\t\tMAC Address\n-----------------------------------------")

    for client in scan_result:
        print(client["ip"] + "\t\t" + client["mac"])



scan_result = scan("192.168.110.2/24")

print_result(scan_result)

