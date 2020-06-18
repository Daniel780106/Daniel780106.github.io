a1=int(input("Please insert number1 here: "))
a2=int(input("Please insert number2 here: "))
result=input("Please pick one calculation: +,-,*,/: ")
if result=="+":
    print(a1+a2)
elif result=="-":
    print(a1-a2)
elif result=="*":
    print(a1*a2)
elif result=="/":
    print(a1/a2)
else:
    print("Wrong picking Calcuation")
