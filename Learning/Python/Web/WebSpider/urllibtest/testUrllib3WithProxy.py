import urllib3
from urllib3 import ProxyManager, make_headers
import sys
import re

def test_argument():
    if len(sys.argv) != 2:
        print('One parameter only.')
        help()
        exit()
    else:
        TP = TestProxy(sys.argv[1])

def help():
    pass

class TestProxy(object):
    '''Check proxy is work'''
    def __init__(self, proxy):
        self.proxy = proxy
        self.check_proxy_format(self.proxy)
        self.url = 'https://malbuffer4pt.github.io'
        self.timeout = 5
        self.flag_word = 'Tools'
        self.use_proxy(self.proxy)

    def check_proxy_format(self, proxy):
        try:
            proxy_match = re.compile('http[s]?://[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}:[\d]{1,5}$')
            re.search(proxy_match, proxy).group()
        except AttributeError:
            help()
            exit()

        flag = 1
        proxy = proxy.replace('//', None)
        try:
            _split = proxy.split(':')
            self.protocol = _split[0]
            self.ip = _split[1]
            self.port = _split[2]
        except IndexError as e:
            print(e)
            help()
            exit()

        #Check proxy format
        ip_split = self.ip.split('.')
        flag = flag and len(_split) == 3 and len(ip_split) == 4
        flag = ip_split[0] in map(str, range(1, 256)) and flag
        flag = ip_split[1] in map(str, range(256)) and flag
        flag = ip_split[2] in map(str, range(256)) and flag
        flag = ip_split[3] in map(str, range(1, 255)) and flag
        flag = self.protocol in [u'http', u'https'] and flag
        flag = self.port in map(str, range(1, 65535)) and flag

        if flag:
            print('Format correct')
        else:
            print('Wrong format')
            help()
            exit()

    def use_proxy(self, proxy):
        '''Access github page with proxy, search key word'''