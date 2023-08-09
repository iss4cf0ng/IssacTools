from scapy.all import *

IFACE_NAME = ''

def dhcp_detect(pkt):
    if DHCP in pkt:
        ls(pkt)
        if pkt[DHCP].options[0][1] == 2:
            ether_request = Ether(src=pkt[Ether].dst, dst='ff:ff:ff:ff:ff:ff')
            ip_request = IP(src='0.0.0.0', dst='255.255.255.255')
            udp_request = UDP(sport=68, dport=67)
            bootp_request = BOOTP(chaddr=pkt[BOOTP].chaddr, xid=pkt[BOOTP].xid)
            dhcp_request = DHCP(options=[('message-type', 'request'), 
                                         ('server_id', pkt[DHCP].options[1][1]),
                                         ('requested_addr', pkt[BOOTP].yiaddr),
                                         'end'])
            request_pkt = ether_request/ip_request/udp_request/bootp_request/dhcp_request
            sendp(request_pkt, IFACE_NAME)

if __name__ == '__main__':
    filter_str = 'src port 67'
    IFACE_NAME = input('Interface > ')
    if not IFACE_NAME:
        IFACE_NAME = '乙太網路'
        print('[*] Interface ->', IFACE_NAME)
    sniff(filter=filter_str, iface=IFACE_NAME, prn=dhcp_detect)