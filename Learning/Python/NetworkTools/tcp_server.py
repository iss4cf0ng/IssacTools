import socket
import threading

IP = "192.168.1.108"
PORT = 5000

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, PORT))
    sock.listen(10)
    print(f'[*] Listening on {IP}:{PORT}')
    
    while True:
        cs, addr = sock.accept()
        print(f'[*] Accept connection from {addr[0]}:{addr[1]}')
        client_handler = threading.Thread(target=handle_event, args=(cs,))
        client_handler.start()
    
def handle_event(cs):
    with cs as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send('ACK') 
    
if __name__ == '__main__':
    main()