a = [1, 2, 3, [4, 5, 6]]
b = a.copy()

def print_address():
    print("Address:")
    print(id(a))
    print(id(b))

def print_elements():
    print("Elements:")
    print(a)
    print(b)

'''
Shallow copy
'''

#First
print_address()
print_elements()

#Second
a[3].append(7)
print_elements() # b also append new element 7

#Third
a.append(8)
print_elements() # b will not append new element 8

'''
Deep copy
'''
import copy
print("=" * 20)
print("Deep copy")
a = [1, 2, 3, [4, 5, 6]]
b = copy.deepcopy(a)
print_address()
a[3].append(7)
print_elements()