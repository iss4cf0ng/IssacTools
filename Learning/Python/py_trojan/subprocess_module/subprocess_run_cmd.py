import subprocess
import sys

def run_command(command):
    command = command.rstrip()
    try:
        child = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    except:
        child = 'Cannot execute the command.\r\n'
    return child

execute = 'nslookup'
output = run_command(execute)
print('*' * 30)
print(sys.getdefaultencoding())
print(output.stdout.decode('big5'))