from scapy.all import *

pkt = IP(dst='192.168.1.1')/ICMP() # Ether(IP(dst='ff:ff:ff:ff:ff:ff'))
ans, uans = sr(pkt)
print(ans.summary())