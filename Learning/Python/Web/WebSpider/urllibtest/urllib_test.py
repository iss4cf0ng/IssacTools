import urllib3
import platform
import os
from http.client import responses

def clear():
    ''' Clear console application text '''
    OS = platform.system()
    if OS == u'Windows':
        os.system('cls')
    else:
        os.system('clear')

def link_page():
    url = 'https://malbuffer4pt.github.io'
    try:
        resp = urllib3.request(url=url, timeout=3, method='GET')
    except urllib3.exceptions.RequestError:
        print('ERROR://')
        exit()

    with open('github.io.txt', 'wb') as fp:
        fp.write(resp.read())

    status_code = resp.status
    status_description = responses[status_code]

    print('Url information :', resp.geturl())
    print('Url status code :', status_code, status_description)
    print('Url msg :', resp.info())
    print('-' * 20)

    http_header_dict = urllib3.HTTPHeaderDict(resp.info())
    print('Content-Length :', http_header_dict['Content-Length'])
    print('Server :', http_header_dict['Server'])

    print('Done')

if __name__ == '__main__':
    link_page()