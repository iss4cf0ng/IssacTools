import sys
if (len(sys.argv) != 2):
    print("[?] Usage : python udp_ping.py IP\r\neg: python udp_ping.py 192.168.1.1")
    exit(1)

from scapy.all import sr, IP, UDP  
ans, unans = sr(IP(dst=sys.argv[1])/UDP(dport=80))
print("-------------")
for snd, recv in ans:
    print(recv.sprintf("%IP.src% is alive!"))
print("-----End-----")