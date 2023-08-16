import paramiko

host = ''
port = 22
user = ''
passwd = ''

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, port=port, username=user, password=passwd)
stdin, stdout, stderr = client.exec_command('ls')
print(stdout.read())