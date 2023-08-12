import re

msg1 = 'Please call my phone : 0911-111-111' # Fake
msg2 = 'This is my phone : 0912-345-678'
msg3 = 'My phone : 0999-999-999 0988-888-888'

def parse_string_findall(string):
    phone_rule = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
    phone_numbers = phone_rule.findall(string=string)
    print('Phone numbers :', phone_numbers)

def parse_string_pattern(string):
    pattern = r'\d{4}-\d{3}-\d{3}'
    phone_number = re.search(pattern=pattern, string=string)
    if phone_number != None:
        print(f'Phone number : {phone_number.group()}')

parse_string_findall(msg1)
parse_string_findall(msg2)
parse_string_findall(msg3)
print('*' * 20)
parse_string_pattern(msg1)
parse_string_pattern(msg2)
parse_string_pattern(msg3)