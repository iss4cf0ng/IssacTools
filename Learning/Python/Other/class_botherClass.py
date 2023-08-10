class Father():
    def __init__(self):
        self.father_money = 10000

class Ira(Father):
    def __init__(self):
        self.ira_money = 8000
        super().__init__()

class Ivan(Father):
    def __init__(self):
        self.ivan_money = 3000
        super().__init__()

    def get_money(self):
        print('Ivan :', self.ivan_money,
              '\nFather :', self.father_money,
              '\nIra :', Ira().ira_money)
        
ivan = Ivan()
ivan.get_money()