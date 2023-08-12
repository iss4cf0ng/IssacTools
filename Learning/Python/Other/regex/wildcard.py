import re

msg = 'Name: ISSAC Address: GitHub respo'
pattern = 'Name: (.*) Address: (.*)'
txt = re.search(pattern, msg)
name, addr = txt.groups()
print('Name:', name)
print('Address:', addr)
print('*' * 20)

# re.DOTALL
msg = 'Name: ISSAC \nAddress: GitHub respo'
pattern = '.*'
txt = re.search(pattern, msg)
print('Output:', txt.group())

txt = re.search(pattern, msg, re.DOTALL)
print('Output:', txt.group())