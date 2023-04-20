s= int(input("enter the salary?"))
if s>=50000:
    print ("tax 40%")
elif s<50000 and s>40000:
    print ("tax 30%")
elif s<40000 and s>30000:
    print ("tax 20%")
elif s<30000 and s>20000:
    print ("tax 10%")
else:
    print ("no tax")
