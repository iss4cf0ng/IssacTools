class Father():
    def hometown(self):
        print('somewhere')

class Son(Father):
    pass

x = Father()
y = Son()
x.hometown()
y.hometown()