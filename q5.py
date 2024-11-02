n=int(input("Enter Number of People in List: "))
l=[]
for i in range(0,n):
    name=input("Enter Name: ")
    l.append(name)
find_name=input("Enetr Name to search: ")
if(find_name in l):
    print(f"{name} in List")
else:
    print(f"{find_name} not in List")
# print(l)