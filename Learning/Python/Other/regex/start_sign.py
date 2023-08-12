import re

msg = 'eat bana1, banana1, banana2, banananananannanan1, banananananana1'
pattern = 'ba(na)*1'
txts = re.search(pattern, msg, re.I)
print(txts.group())