loan = eval(input("貸款金額: "))
year = eval(input("貸款年限: "))
rate = eval(input("年利率: "))
month_rate = rate / (12*100) #Percentage, monthly

molecules = loan * month_rate
denominator = 1 - (1/(1+month_rate)) ** (year * 12)
monthly_pay = molecules / denominator
total_pay = monthly_pay * year * 12

print(f'每月還錢 {int(monthly_pay)}')
print(f'總共還錢 {int(total_pay)}')