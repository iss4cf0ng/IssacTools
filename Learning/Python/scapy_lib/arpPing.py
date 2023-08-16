from scapy.all import *

tgt_ipv4 = '192.168.1.1/24'
eth_pkt = Ether(dst='ff:ff:ff:ff:ff:ff')
arp_pkt = ARP(pdst=tgt_ipv4)
pkt = eth_pkt/arp_pkt
ans, unans = srp(pkt, timeout=1)
for s, r in ans:
    print('Target is alive')
    print(r.sprintf('%Ether.src% - %ARP.psrc%'))