from scapy.all import *

ls(DNS())
print('-' * 20)
ls(DNSQR)
print('-' * 20)

'''Flags'''
qr = 0 # Search query
opcode = 0 # Standard search
rd = 1 # Recursive search

'''Quries'''
qd = DNSQR(qname='google.com')

pkt = IP(dst='192.168.1.1')/UDP(dport=53)/DNS(id=168, qr=qr, opcode=opcode, qd=qd)
ls(pkt)
print('-' * 20)

dns_result = sr1(pkt) # Receive one packet only, do not use sendp because the destination ip is not MAC address
ls(dns_result)
dns_result_ip = dns_result.getlayer(DNS).fields['an'][0].fields['rdata'] # dns_result[DNS].an[0].rdata
print(dns_result_ip)