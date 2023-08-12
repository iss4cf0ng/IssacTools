import re

# Test1
msg = 'Please call my phone : 02-11112222'
pattern = r'(\d\d-)?(\d{8})'
phone_number = re.search(pattern, msg)
print(f'Full number : {phone_number.group()}')

# Test2
msg = 'Please call my phone : 11112222'
phone_number = re.search(pattern, msg)
print(f'Full number : {phone_number.group()}')