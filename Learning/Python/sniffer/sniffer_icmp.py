import socket
import ipaddress
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
  
class ICMP:
    def __init__(self, buff=None):
        header = struct.unpack('<BBHHH', buff)
        self.type = header[0]
        self.code = header[1]
        self.sum = header[2]
        self.id = header[3]
        self.seq = header[4]
    
def sniff(host):
    if os.name == 'nt':
        pass
    else:
        pass
    
if __name__ == '__main__':
    pass