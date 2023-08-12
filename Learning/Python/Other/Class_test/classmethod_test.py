class Counter():
    counter = 0
    def __init__(self):
        Counter.counter += 1

    @classmethod # Error if not use @classmethod
    def show_counter(cls):
        print('Class method')
        print('counter =', cls.counter)
        print('counter =', Counter.counter)
    '''
    TypeError: Counter.show_counter() missing 1 required positional argument: 'cls'
    '''

    @staticmethod
    def say_hello():
        print(Counter.counter)
        print('Hello world')

x = Counter()
y = Counter()
z = Counter()
Counter.show_counter()
Counter.say_hello()