import re

msg = 'Please call my secretary using 02-11111111'
pattern = r'(\d{2})-(\d{8})'
phone_number = re.search(pattern, msg)
print(phone_number.group())
print(phone_number.group(0))
print(phone_number.group(1))
print(phone_number.group(2))