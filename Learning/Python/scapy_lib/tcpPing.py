from scapy.all import *

tgt_ipv4 = '192.168.1.1'
tgt_port = 80
ip_pkt = IP(dst=tgt_ipv4)
tcp_pkt = TCP(dport=tgt_port, flags=0x012)
pkt = ip_pkt/tcp_pkt
ans, un_ans = sr(pkt, timeout=2)
for s, r in ans:
    print(r.sprintf('%IP.src% is alive'))
for s in un_ans:
    print('Target is not alive.')