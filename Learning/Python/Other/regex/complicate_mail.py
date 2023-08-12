import re

msg = 'txt@asdqweqwe.com.tw someone@gmail.com'
pattern = r'((\w+)@([a-zA-Z0-9_]+)[\.]\w{2,4}(\.)?(\w{2,4})?)'
txt = re.findall(pattern, msg, re.VERBOSE)
for i in txt:
    print(i[0])