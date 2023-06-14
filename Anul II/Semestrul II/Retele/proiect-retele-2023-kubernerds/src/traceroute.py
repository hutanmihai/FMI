import socket
import sys
import struct
from time import time
import requests
import os
from geopy.geocoders import Nominatim
import folium
import webbrowser


def checksum(data):
    if len(data) % 2:
        data += b"\x00"
    words = struct.unpack("!%sH" % (len(data) // 2), data)
    total = sum(words)
    while total >> 16:
        total = (total & 0xFFFF) + (total >> 16)
    total = socket.htons(total)
    return ~total & 0xFFFF


def build_packet():
    icmp_type = 8  # tipul de pachet ICMP de tip Echo Request
    icmp_code = 0  # codul de pachet ICMP de tip Echo Request
    icmp_checksum = 0  # checksum-ul de pachet ICMP de tip Echo Request
    icmp_identifier = 12345  # identificatorul ICMP
    icmp_sequence = 1  # secvența ICMP
    icmp_data = b"test"
    icmp_payload = struct.pack("d", 0.0)  # payload-ul ICMP
    icmp_header = struct.pack(
        "bbHHh", icmp_type, icmp_code, icmp_checksum, icmp_identifier, icmp_sequence
    )

    icmp_packet = icmp_header + icmp_data + icmp_payload

    icmp_checksum = checksum(icmp_packet)
    icmp_header = struct.pack(
        "bbHHh", icmp_type, icmp_code, icmp_checksum, icmp_identifier, icmp_sequence
    )
    icmp_packet = icmp_header + icmp_data + icmp_payload
    return icmp_packet


def get_location(ip):
    endpoint = f"https://ipinfo.io/{ip}/json"
    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        try:
            hostname = data.get("hostname")
        except KeyError:
            hostname = "Unknown"
        if city is None:
            return None, "Unknown"
        else:
            return f"{city}, {region}, {country}", hostname
    else:
        return None, "Unknown"


def traceroute(host, max_hops=30):
    dest_address = socket.gethostbyname(host)
    locations = []
    count = 0
    ips = set()
    for ttl in range(1, max_hops + 1):
        icmp_socket = socket.socket(
            socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP
        )
        icmp_socket.settimeout(5)
        icmp_socket.bind(("", 33434))  # port de baza pentru traceroute
        icmp_socket.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, struct.pack("I", ttl))
        try:
            packet = build_packet()
            icmp_socket.sendto(packet, (host, 33434))
            start_time = time()
            data, address = icmp_socket.recvfrom(1024)
            end_time = time()
            elapsed_time = (end_time - start_time) * 1000
            if address[0] not in ips:
                count += 1
                ips.add(address[0])
                location, address_name = get_location(address[0])
                if location is not None:
                    print(
                        f"{count}. {address[0]} ({address_name}) {location} {elapsed_time:.3f} ms"
                    )
                    if location not in locations:
                        locations.append(location)
                else:
                    print(
                        f"{count}. {address[0]} ({address_name}) {elapsed_time:.3f} ms"
                    )
            if dest_address == address[0]:
                break

        except socket.timeout:
            count += 1
            print(f"{count}. timed out")
        except socket.error as e:
            print(e)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt: Traceroute stopped.")
            sys.exit(1)
        finally:
            icmp_socket.close()

    CURR_PATH = os.getcwd()
    i = 0
    while os.path.exists(os.path.join(CURR_PATH, f"output{i}.txt")):
        i += 1
    with open(f"output{i}.txt", "w") as out:
        for location in locations:
            out.write(f"{location}\n")
        out.close()
    return f"output{i}.txt"


#   Am folosit ChatGPT pentru a imi genera o harta cu locatiile
#   https://chat.openai.com/share/d8103d5a-f0c0-4fcf-8727-db9b5bd747f3
def plot_traceroute(locations): 
    if len(locations) == 0:
        print("No locations to plot.")
        return

    geolocator = Nominatim(user_agent="my-custom-user-agent")
    coordinates = []
    for location in locations:
        loc = geolocator.geocode(location)
        coordinates.append((loc.latitude, loc.longitude))

    m = folium.Map(location=coordinates[0], zoom_start=3)
    for i, coord in enumerate(coordinates):
        folium.Marker(location=coord, tooltip=locations[i]).add_to(m)

    for i in range(len(coordinates) - 1):
        origin = coordinates[i]
        destination = coordinates[i + 1]
        pattern = [i for i in range(1, 11)] + [0] * 10
        line = folium.PolyLine(
            locations=[origin, destination], color="blue", dash_array=pattern
        )
        m.add_child(line)

    m.save("traceroute_map.html")
    webbrowser.open("traceroute_map.html")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python traceroute.py <host>")
        sys.exit(1)
    elif len(sys.argv) == 3:
        output_file = traceroute(sys.argv[1], int(sys.argv[2]))
    else:
        output_file = traceroute(sys.argv[1])
    locations = open(output_file, "r").readlines()
    plot_traceroute(locations)
