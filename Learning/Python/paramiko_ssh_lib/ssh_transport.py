import paramiko

host = ''
port = 22
user = ''
passwd = ''

transport = paramiko.Transport((host, port))
transport.connect(username=user, password=passwd)

# create sftp
sftp = paramiko.SFTPClient().from_transport(transport)

# upload location.py to '/tmp/server_file.py'
sftp.put('/tmp/location.py', '/tmp/server_file.py')

# download server_file.py to local :
sftp.get('server_file.py', 'local_path')
transport.close()