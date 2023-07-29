#pip install paramiko
import paramiko
import getpass

def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, port=port, username=user, password=passwd)
    
    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('-----Output-----')
        for line in output:
            print(line.strip())
            
if __name__ == '__main__':
    #user = getpass.getuser()
    user = input('Username: ')
    passwd = input('Password: ')
    ip = input('IP: ')
    port = int(input('Port: '))
    while True:
        cmd = input('Shell>')
        if cmd == 'exit':
            break
        ssh_command(ip, port, user, passwd, cmd)