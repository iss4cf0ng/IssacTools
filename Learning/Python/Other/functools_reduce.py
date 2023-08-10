from functools import reduce

sum1 = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
print(sum1)