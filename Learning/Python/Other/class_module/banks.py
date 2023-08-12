#banks.py
class Banks():
    '''define Banks class'''
    def __init__(self, username):
        self.__name = username
        self.__balance = 0
        self.__title = 'Taipei Bank'

    def save_money(self, money):
        self.__balance += money
        print('Save money %s successfully' % money)

    def withdraw_money(self, money):
        self.__balance -= money
        print('Withdraw money %s successfully.' % money)

    def get_balance(self):
        print('Balance :', self.__balance)

    def bank_title(self):
        return self.__title

class Shilin_Banks(Banks):
    '''Shilin Banks class'''
    def __init__(self):
        self.title = 'Taipei Bank - Shilin Branch'

    def bank_title(self):
        return self.title