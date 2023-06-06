class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name= name
        mysillyobject.age= age
    def myfunction(mysillyobject):
        print("Hello my name is" + mysillyobject.name)
        print(" age is", mysillyobject.age)

a=Person("xxx",45)
a.myfunction()
