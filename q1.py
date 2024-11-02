a1=int(input(f"Enter 1st Number: "))
a2=int(input(f"Enter 2nd Number: "))
a3=int(input(f"Enter 3rd Number: "))
a4=int(input(f"Enter 4th Number: "))

if(a1>a2 & a1>a3 & a1>a4):
    print(f"{a1} is the largest number")
elif(a2>a1 & a2>a3 & a2>a4):
    print(f"{a2} is the largest number")
elif(a3>a1 & a3>a2 & a3>a4):
    print(f"{a3} is the largest number")
else:
    print(f"{a4} is the largest number")
