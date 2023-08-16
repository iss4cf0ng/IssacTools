from scapy.all import *

tgt = '192.168.1.111'
ip_pkt = IP(dst=tgt)
pkt = ip_pkt/ICMP()
ans, un_ans = sr(pkt, timeout=1)
for s, r in ans:
    print(r.sprintf('%IP.src% is alive'))