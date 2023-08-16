import subprocess

res = subprocess.run(['cd', 'C:'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
print(type(res))
print(res)
print(f'code: {res.returncode} stdout: {res.stdout}')