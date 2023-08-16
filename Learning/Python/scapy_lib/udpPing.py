from scapy.all import *

tgt_ip = '192.168.1.1'
tgt_port = 80
pkt = IP(dst=tgt_ip)/UDP(dport=tgt_port)
ans, un_ans = sr(pkt, timeout=2)
ans.summary(lambda s, r : r.sprintf('%IP.src% is alive'))