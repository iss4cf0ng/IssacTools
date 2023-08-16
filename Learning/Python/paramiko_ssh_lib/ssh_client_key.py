import paramiko

host = ''
port = 22
user = ''

private_key_path = '/home/issac/.ssh/id_rsa'
key = paramiko.RSAKey().from_private_key(private_key_path)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, port=port, username=user, pkey=key)
stdin, stdout, stderr = client.exec_command('ls')
print(stdin.read())