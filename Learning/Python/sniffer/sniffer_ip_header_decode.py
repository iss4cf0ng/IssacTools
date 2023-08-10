import ipaddress
import socket
import struct
import os
import sys

class IP:
    def __init__(self, buff=None):
        header = struct.unpack('<BBHHHBBH4s4s', buff)
        self.ver = header[0] > 4
        self.ihl = header[0] and 0xf
        
        self.tos = header[1] # type of service
        self.len = header[2] # total length
        self.id = header[3] # identificiation
        self.offset = header[4] # fragment offset
        self.ttl = header[5] # time to live
        self.protocol_num = header[6] # protocol number
        self.sum = header[7] # checksum
        self.src = header[8] # source (ip)
        self.dst = header[9] # destination (ip)
        
        self.src_address = ipaddress.ip_address(self.src) # readable ip address
        self.dst_address = ipaddress.ip_address(self.dst) # readable ip address
        
        self.protocol_map = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}
        self.protocal = None
        try:
            self.protocal = self.protocol_map[self.protocol_num]
        except Exception as e:
            print('No protocol for %s' % self.protocol_num)
            self.protocol = self.protocol_num
            
def sniff(host):
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP
        
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((host, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        
    while True:
        try:
            raw_buffer = sniffer.recvfrom(65535)[0]
            ip_header = IP(raw_buffer[0:20])
            print(f'Protocol:{ip_header.protocal} {ip_header.src_address} -> {ip_header.dst_address}')
        except KeyboardInterrupt:
            if os.name == 'nt':
                sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
            break
    sys.exit()
        
if __name__ == '__main__':
    if len(sys.argv) == 2:
        host = sys.argv[1]
    sniff(host)