import socket
import argparse
import shlex
import sys
import subprocess
import textwrap
import threading

class NetCat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()
            
    def send(self):
        print("Start connection...")
        self.socket.connect((self.args.target, self.args.port))
        print("Connect successfully!")
        if self.buffer:
            self.socket.send(self.buffer)
            
        try:
            recv_len = 1
            response = ''
            while recv_len:
                data = self.socket.recv(4096)
                recv_len = len(data)
                response += data.decode()
                if recv_len < 4096:
                    break
            if response:
                print(response)
                buffer = input('> ')
                buffer += '\n'
                self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print("User terminated")
            self.socket.close()
            sys.exit()
            
    def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        print("Start listening...")
        while True:
            client_socket, addr = self.socket.accept()
            client_thread = threading.Thread(
                target=self.handle, args=(client_socket,)
            )
            client_thread.start()
            
    def handle(self, client_socket):
        if self.args.execute:
            output = execute(self.args.execute)
            client_socket.send(output.encode())
        elif self.args.upload:
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break
            
            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)
            msg = f'Save file successfully!{self.args.upload}'
            client_socket.send(msg.encode())
        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    prompt = 'BHP: #> '
                    client_socket.send(prompt.encode())
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(4096)
                    print(cmd_buffer.decode())
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'Server killed {e}')
                    client_socket.close()
                    sys.exit()

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="BHP Net Tool",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=textwrap.dedent(
            '''
            Example:

            '''
        )
    )
    parser.add_argument('-c', '--command', action="store_true", help="Run command")
    parser.add_argument('-e', '--execute', help="Execute specific command")
    parser.add_argument('-l', '--listen', action="store_true", help="Listen port")
    parser.add_argument('-p', '--port', type=int, default=5555, help="specified port")
    parser.add_argument('-t', '--target', default="localhost", help="specified target")
    parser.add_argument('-u', '--upload', help="Upload file")
    args = parser.parse_args()
    
    if args.listen:
        buffer = ''
    else:
        #buffer = sys.stdin.read()
        buffer = ''
        
    nc = NetCat(args=args, buffer=buffer.encode())
    nc.run()