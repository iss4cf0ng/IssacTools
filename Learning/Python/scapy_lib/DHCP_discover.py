from scapy.all import *
import binascii

'''
DHCP test, last version of DHCP is Bootstrap
DHCP using UDP
DHCP server port : 67
DHCP client port : 68

DHCP Process:
1.DHCP discover packet (client -> server)
2.DHCP offer (server -> client)
3.DHCP request (client -> server)
4.DHCP ACK packet (server -> client)

scapy packet structure (DHCP packet standard):
Ether -> IP -> UDP -> BOOTP -> DHCP
'''

def ls_DHCP_BOOTP():
    pkt = DHCP()
    ls(pkt)
    print('-' * 20)
    pkt = BOOTP()
    ls(pkt)

# DHCP boardcast Discover packet
mac_random = str(RandMAC())
ether_discover = Ether(src=mac_random, dst='ff:ff:ff:ff:ff:ff')
# No IP address, using 0.0.0.0
ip_discover = IP(src='0.0.0.0', dst='255.255.255.255')
# Client port : 68, Server port : 67
udp_discover = UDP(sport=68, dport=67)
ls_DHCP_BOOTP()
# In BOOTP, mac address will not use ':'
# xid is necessary, but can be random
client_mac_id = binascii.unhexlify(mac_random.replace(':', '')) # client mac id must be in byte format in bootstrap
xid_random = random.randint(1, 10000)
bootp_discover = BOOTP(chaddr=client_mac_id, xid=xid_random)
# Finally, DHCP packet
dhcp_discover = DHCP(options=[('message-type', 'discover'), 'end'])

discover = ether_discover/ip_discover/udp_discover/bootp_discover/dhcp_discover

interface_name = input('Interface > ')
if not interface_name:
    interface_name = '乙太網路'
print('[*] Interface ->', interface_name)
sendp(discover, iface=interface_name)