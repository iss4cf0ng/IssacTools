from collections import Counter

fruits = ['apple', 'orange', 'apple']
fruits_dict = Counter(fruits)
print(fruits_dict)
print('*' * 20)
fruits1 = ['apple', 'orange', 'apple']
fruits2 = ['apple', 'orange', 'banana', 'grape']
fruitsA = Counter(fruits1)
fruitsB = Counter(fruits2)
fruits_add = fruitsA + fruitsB
print(fruits_add)
fruits_sub = fruitsB + fruitsA
print(fruits_sub)