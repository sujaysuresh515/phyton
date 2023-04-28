a=4
def name():
    global b
    b=3
    global c
    c=a+b
    print(c)
name()
print(a)
print(b)
print(c)
