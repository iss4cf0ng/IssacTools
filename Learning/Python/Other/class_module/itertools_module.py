import itertools

print('chain()')
for i in itertools.chain([1, 2, 3],[[4,5],6], ('a', 'b', [1, 2])):
    print(i)

'''
print('cycle()')
for i in itertools.cycle(([1, 2], 3)):
    print(i)
'''

print('accumulate()')
def multi(x, y):
    return x
for i in itertools.accumulate([1, 2, 3, 4, 5]):
    print(i)
for i in itertools.accumulate((1, 2, 3, 4, 5), multi):
    print(i)

print('combination')
x = ['x', 'y', 'z', 'x', 'y']
r = 2
y = itertools.combinations(x, r)
print(list(y))
result1 = []
result2 = []
max_length = 3
string = 'abcde'
for i in range(1, max_length + 1):
    result1 += itertools.combinations(list(string), i)
    result2 += list(itertools.combinations(list(string), i))
print(result1)
print(result2)