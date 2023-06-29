import sys
if (len(sys.argv) != 2):
    print("[?] Usage : python icmp_ping.py IP\r\neg: python icmp_ping.py 192.168.1.1")
    exit(1)
    
from scapy.all import sr, IP, ICMP
ans, unans = sr(IP(dst=sys.argv[1]), timeout=2)
print("-------------")
for snd, recv in ans:
    print(recv.sprintf("%IP.src% is alive"))
print("-----End-----")