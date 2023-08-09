from scapy.all import sniff

def packet_callback(packet):
    print(packet.show())
    
def main():
    filter_str = 'tcp port 80 or tcp port 443'
    sniff(prn=packet_callback, count=1, filter=filter_str)
    
if __name__ == '__main__':
    main()