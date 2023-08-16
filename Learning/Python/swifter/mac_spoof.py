from scapy.all import *
import time
import uuid

IFACE = input('')
if not IFACE:
    IFACE = '乙太網路'

def get_self_mac():
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
    print(mac)
    return ':'.join(mac[x:x+2] for x in range(0, 11, 2))

while 1:
    eth_pkt = Ether(src=get_self_mac(), dst=RandMAC())
    ip_pkt = IP(src=RandIP(), dst=RandIP())
    pkt = eth_pkt/ip_pkt/ICMP()
    time.sleep()
    sendp(pkt, iface=IFACE, loop=0)