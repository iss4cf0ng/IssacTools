from bs4 import BeautifulSoup as bs
import requests

url = 'https://malbuffer4pt.github.io'
r = requests.get(url=url)
tree = bs(r.text, 'html.parser')
for link in tree.find_all('a'):
    print(f"{link.get('href')} -> {link.text}")