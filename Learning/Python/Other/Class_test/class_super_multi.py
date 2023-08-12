class A():
    def __init__(self):
        super().__init__()
        print('class A')

class B():
    def __init__(self):
        super().__init__()
        print('class B')

class C(A, B):
    def __init__(self):
        super().__init__()
        print('class C')

x = C()