a = 10
b = 10

def print_address():
    print("Address:")
    print(id(a))
    print(id(b))

def print_elements():
    print("Elements:")
    print(a)
    print(b)

print_address()
b = 20
print_elements()
print_address()