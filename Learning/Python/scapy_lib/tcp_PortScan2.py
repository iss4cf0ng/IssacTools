from scapy.all import *

dst_ip = '192.168.1.1'
src_port = RandShort()
dst_port = 80
pkt = IP(dst=dst_ip)/TCP(sport=src_port, dport=dst_port, flags='S')
resp = sr1(pkt, timeout=2)
if str(type(resp)) == "<class 'NoneType'>":
    print(f'Port {dst_port} is closed')
elif resp.haslayer(TCP):
    if resp.getlayer(TCP).flags == 0x12:
        print(f'Port {dst_port} is open')
    elif resp.getlayer(TCP).flags == 0x14:
        print(f'Port {dst_port} is closed')