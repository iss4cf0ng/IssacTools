from banks import Banks, Shilin_Banks

james_bank = Banks('James')
print("James's banks =", james_bank.bank_title())
james_bank.save_money(10000)
james_bank.get_balance()