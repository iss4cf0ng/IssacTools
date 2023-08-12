import re

msg = 'CIA Mark told CIA Linda that secret USB had given to cIa Peter.'
pattern = r'[cC][iI][aA] (\w)\w*' # Since upper case
new_str = r'\1***'
txt = re.sub(pattern, new_str, msg)
print(txt)