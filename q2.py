marks1= int(input("enter marks 1: "))
marks2= int(input("enter marks 2: "))
marks3= int(input("enter marks 3: "))

total_percentage=(100*(marks1+marks2+marks3))/300
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print(f"pass with {total_percentage}")
else:
    print(f"Fail!! with {total_percentage}")
    