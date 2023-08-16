import subprocess

child = subprocess.Popen(['ping', 'github.com'])
print('Parent process')