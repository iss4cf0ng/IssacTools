import re

msg = '121238797409173809123'
pattern = '^\d+$'
txt = re.findall(pattern, msg)
print(txt)
msg = '123890as9d78-09'
txt = re.findall(pattern, msg)
print(txt)