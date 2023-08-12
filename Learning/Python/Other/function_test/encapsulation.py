class Banks():
    def __init__(self, uname):
        self.__name = uname
        self.__balance = 0

    def get_balance(self):
        print('%s : %s' % (self.__name, self.__balance))

my_bank = Banks('issac')
my_bank.get_balance()
my_bank.__balance = 10000
my_bank.get_balance()
my_bank._Banks__balance = 12000
my_bank.get_balance()