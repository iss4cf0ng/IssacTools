import sys
if (len(sys.argv) != 2):
    print("[?] Usage : python arp_ping.py IP\r\neg: python arp_ping.py 192.168.1.1")
    exit(1)

from scapy.all import srp, ARP, Ether 
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sys.argv[1]), timeout=2)
print("-------------")
for snd, recv in ans:
    print("Target alive:")
    print(recv.sprintf("%Ether.src% - %ARP.psrc%"))
print("-----End-----")