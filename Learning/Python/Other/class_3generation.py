class GrandFather():
    def __init__(self):
        self.grandfather_money = 10000
    
    def get_info1(self):
        print('Grandfather information')

class Father(GrandFather):
    def __init__(self):
        self.father_money = 8000
        super().__init__()

    def get_info2(self):
        print('Father information')

class Ivan(Father):
    def __init__(self):
        self.ivan_money = 3000
        super().__init__()

    def get_info3(self):
        print('Ivan information')

    def get_money(self):
        print('Grandfather money : %s\nFather money : %s\nIvan money : %s' % (self.grandfather_money, self.father_money, self.ivan_money))

ivan = Ivan()
ivan.get_info3()
ivan.get_info2()
ivan.get_info1()
ivan.get_money()