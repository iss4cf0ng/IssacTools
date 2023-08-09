from scapy.all import *

pkt = Ether()/IP(src='192.168.1.108', dst='20.27.177.113', ttl=32)/TCP()
print(pkt)
ls(pkt)  # Show packet detail
print('-' * 20)

print(raw(pkt))  # Show packet with bytes
print('-' * 20)

print(hexdump(pkt))  # Display packet hexdump
print('-' * 20)

print("Summary")
print(pkt.summary())
print('-' * 20)

print('Show')
print(pkt.show())
print('-' * 20)

print('Show2')
print(pkt.show2())
print('-' * 20)

print('command')
print(pkt.command())
print('-' * 20)