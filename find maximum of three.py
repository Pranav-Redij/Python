#finding max of three number 
a=int(input("enter the a:"))
b=int(input("enter the b:"))
c=int(input("enter the c:"))

if(a>b and a>c):
    print(a," is max")
elif b>c:
    print(b," is max")
else:
    print(c," is max")