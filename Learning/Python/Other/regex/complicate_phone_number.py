import re

msg = '''
02-11112222, (02)-22223333, 02-88889999 ext 123, 12345678, 02 33887766 ext. 12222
'''
pattern = r'''(
    (\d{2}|\(\d{2}\))?
    (\s|-)?
    (\d{8})
    (\s*(ext|ext.)\s*\d{2,4})?
    )'''

#((\d{2}|\(\d{2}\))?(\s|-)?(\d{8})(\s*(ext|ext.)\s*\d{2,4})?)
phone_number = re.findall(pattern, msg, re.VERBOSE)
print(phone_number)
for i in phone_number:
    print(i[0])