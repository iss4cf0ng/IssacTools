import sys
if (len(sys.argv) != 3):
    print("[?] Usage : python tcp_ping.py IP Port\r\neg: python tcp_ping.py 192.168.1.1 80")
    exit(1)

from scapy.all import sr, IP, TCP
ans, unans = sr(IP(dst=sys.argv[1])/TCP(dport=sys.argv[2], flags="S"))
print("-------------")
for snd, recv in ans:
    print(recv.sprintf("%IP.src% is alive!"))
print("-----End-----")