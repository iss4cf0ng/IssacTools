from scapy.all import *

FILTER = input('Filter > ')
if FILTER:
    sniff(filter=FILTER, count=10, prn=lambda x: ls(x))