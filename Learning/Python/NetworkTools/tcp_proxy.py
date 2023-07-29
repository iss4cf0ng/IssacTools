import socket
import sys
import threading

HEX_FILTER = ''.join(
    [
        (len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)
    ]
)

def hexdump(src, length=16, show=True):
    if isinstance(src, bytes):
        src = src.decode()
    results = list()
    for i in range(0, len(src), length):
        word = str(src[i:i+length])
        
        printable = word.translate(HEX_FILTER)
        hexa = ' '.join([f'{ord(c):02X}' for c in word])
        hexwidth = length * 3
        results.append(f'{i:04X} {hexa:<{hexwidth}} {printable}')
    if show:
        for line in results:
            print(line)
    else:
        return results
    
def receive_from(connection):
    _buffer = b''
    connection.settimeout(5)
    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            _buffer += data
    except Exception as e:
        print(e)
    return _buffer

def request_handler(_buffer):
    
    return _buffer

def response_handler(_buffer):
    
    return _buffer

def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
    remote_socket.connect((remote_host, remote_port))
    
    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)
        
    remote_buffer = response_handler(remote_buffer)
    if len(remote_buffer):
        print('[<==] Sending %s bytes to localhost' % len(remote_buffer))
        client_socket.send(remote_buffer)
    
    while True:
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            msg = '[==>] Received %s bytes from localhost' % len(local_buffer)
            print(msg)
            hexdump(local_buffer)
            
            local_buffer = request_handler(local_buffer)
            remote_socket.send(local_buffer)
            print('[==>] Sent to remote')
            
        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            print('[<==] Received %s bytes from remote' % len(remote_buffer))
            hexdump(remote_buffer)
            
            remote_buffer = request_handler(remote_buffer)
            client_socket.send(remote_buffer)
            print('[<==] Sent to localhost.')
            
        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print('[*] No more data, connection closed')
            break
        
def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((local_host, local_port))
    except Exception as e:
        sys.exit(0)
        
    print('[*] Listening on %s:%s' % (local_host, local_port))
    server.listen(5)
    while True:
        client_socket, addr = server.accept()
        print('> Received incoming connection from %s:%s' % (addr[0], addr[1]))
        proxy_thread = threading.Thread(target=proxy_handler, args=(client_socket, remote_host, remote_port, receive_first,))
        proxy_thread.start()

def print_help():
    print()

def main():
    if len(sys.argv[1:]) != 5:
        print_help()
        sys.exit(0)
    local_host = sys.argv[1]
    local_port = sys.argv[2]
    remote_host = sys.argv[3]
    remote_port = sys.argv[4]
    receive_first = sys.argv[5]
    
    if "True" in receive_first:
        receive_first = True
    else:
        receive_first = False
        
    server_loop(local_host, local_port, remote_host, remote_port, receive_first)

if __name__ == '__main__':
    main()