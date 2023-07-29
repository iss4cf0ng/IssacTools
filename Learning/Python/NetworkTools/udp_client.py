import socket

target_ip = "localhost"
target_port = 5000

msg = "Hello world"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
sock.sendto(msg.encode("utf-8"), (target_ip, target_port))
data, addr = sock.recvfrom(4096)
print("%s > %s" % (addr, data.decode("utf-8")))
sock.close()