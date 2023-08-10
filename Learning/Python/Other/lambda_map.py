mylist = [1, 2, 3, 4, 5, 9]

square_list = list(map(lambda x : eval(x) ** 2, '123'))
print(square_list)
square_list = list(map(lambda x : x ** 2, mylist))
print(square_list)