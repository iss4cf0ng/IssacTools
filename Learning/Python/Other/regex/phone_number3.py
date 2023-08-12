import re

msg = 'My phone (02)-11112222'
pattern = r'(\(\d{2}\))-(\d{8})'
phone_num = re.search(pattern, msg)
area_num, local_num = phone_num.groups()
print('Area:', area_num)
print('Local:', local_num)