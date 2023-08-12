import re

msg = 'John and Tom will attend my party tonight. John is my best friend.'
pattern = 'John|Tom'
txt = re.findall(pattern, msg)
print(txt)
pattern = 'Mary|Tom'
txt = re.findall(pattern, msg)
print(txt)

msg = 'Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = 'John(son|nason|nathan)'
txt = re.search(pattern, msg)
print(txt.group())
print(txt.group(1))

txts = re.findall(pattern, msg)
print(txts)
for i in txts:
    print('John' + i)