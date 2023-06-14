FROM snisioi/retele:2021

RUN apt-get update && apt-get install -y iptables iproute2 libnetfilter-queue-dev dsniff

RUN pip3 install --upgrade python-iptables cython

RUN pip3 install geopy folium

RUN mkdir -p /scripts

COPY src/* /scripts/
