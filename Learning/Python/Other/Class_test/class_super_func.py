class Animals():
    '''Class Animal, base class'''
    def __init__(self, animal_name, animal_age):
        self.name = animal_name
        self.age = animal_age

    def run(self):
        print(self.name.title(), 'is running')

class Dogs(Animals):
    def __init__(self, dog_name, dog_age):
        super().__init__('My pet ' + dog_name.title(), dog_age)

mycat = Animals('lucy', 5)
print(mycat.name.title(), 'is', mycat.age, 'years old')
mycat.run()

mydog = Dogs('luck', 6)
print(mydog.name.title(), 'is', mydog.age, 'years old')
mydog.run()