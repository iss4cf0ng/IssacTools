import re

def search_str(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:
        print('Failed')
    else:
        print('Found :', txt.group())

msg = 'sonsonsonsonson'
pattern = '(son){3,5}' # greedy
search_str(pattern, msg)

pattern = '(son){3,5}?'
search_str(pattern, msg) # Non greedy