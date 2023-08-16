from scapy.all import *

dst_ip = '192.168.1.1'
src_port = RandShort()
dst_port = 80
pkt = IP(dst=dst_ip)/TCP(sport=src_port, dport=dst_port, flags='S')
resp = sr1(pkt, timeout=1)
if str(type(resp)) == "<class 'NoneType'>":
    print('Port %s is closed' % dst_port)
elif resp.haslayer(TCP):
    if resp.getlayer(TCP).flags == 0x12:
        seq1 = resp.ack
        ack1 = resp.seq + 1
        pkt_rst = IP(dst=dst_ip)/TCP(sport=src_port, dport=dst_port, flags=0x10, seq=seq1, ack=ack1)
        send(pkt_rst)
        print('The port %s is open' % dst_port)
    elif resp.getlayer(TCP).flags == 0x14:
        print('The port %s is closed' % dst_port)