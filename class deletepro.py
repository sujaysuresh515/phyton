class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    def myfunction(self):
        print("Hello my name is" + self.name)
        print(" age is", self.age)

a=Person("xxx",45)

del a.age
print(a.age)
