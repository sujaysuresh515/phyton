class Person:
    def __init__(self,a,b):
        self.a= a
        self.b= b
    def myfunction(self):
        c= self.a+self.b
        print(c)
a=Person(751,45)
a.myfunction()

