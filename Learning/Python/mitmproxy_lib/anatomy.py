from mitmproxy import http, ctx

class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num += 1
        ctx.log.info("We've seen %d flows" % self.num)

addons = [
    Counter()
    
]

'''
mitmdump -s ./anatomy.py
'''