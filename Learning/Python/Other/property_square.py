class Square():
    def __init__(self, side_len):
        self.__side_len = side_len

    @property
    def area(self):
        return self.__side_len ** 2
    
obj = Square(10)
print(obj.area) # It is different to obj.area()