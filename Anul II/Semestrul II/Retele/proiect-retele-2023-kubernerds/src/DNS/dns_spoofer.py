from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sniff, send

ADSERVERS_PATH = "adservers.txt"
COINMINERS_PATH = "CoinMiner.txt"
FACEBOOK_PATH = "facebook.txt"
OUTPUT_PATH = "blocked_domains.txt"


def parse_blocked_domains_file():
    files = [ADSERVERS_PATH, COINMINERS_PATH, FACEBOOK_PATH]
    domains = []
    for file in files:
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("#"):
                    continue
                line = line.lstrip("0.0.0.0").strip("\n").strip()
                domains.append(line)
    return domains


BLOCKED_DOMAINS = parse_blocked_domains_file()


def handle_packet(packet):
    if packet.haslayer(DNSQR) and packet[DNS].qr == 0:
        queried_domain = packet[DNSQR].qname.decode("utf-8")[:-1]
        if queried_domain in BLOCKED_DOMAINS:
            with open(OUTPUT_PATH, "a") as f:
                f.write(f"{queried_domain}\n")
            print(f"DNS request for {queried_domain} blocked!")
            dns_answer = DNSRR(rrname=packet[DNS].qd.qname, rdata="0.0.0.0")
            spoofed_packet = (
                    IP(dst=packet[IP].src, src=packet[IP].dst)
                    / UDP(dport=packet[UDP].sport, sport=packet[UDP].dport)
                    / DNS(id=packet[DNS].id, qr=1, aa=1, qd=packet[DNS].qd, an=dns_answer)
            )
            send(spoofed_packet)
        else:
            print(f"DNS request for {packet[DNSQR].qname.decode('utf-8')} allowed!")


sniff(filter="udp port 53", prn=handle_packet, promisc=False)
