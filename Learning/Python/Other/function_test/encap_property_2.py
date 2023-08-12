class Score():
    def __init__(self, score):
        self.__score = score

    def getscore(self):
        print('inside the getscore')
        return self.__score
    
    def setscore(self, score):
        print('Inside the setscore')
        self.__score = score
    sc = property(getscore, setscore)

stu = Score(0)
print(stu.sc)
print('*' * 20)
stu.sc = 80
print(stu.sc)