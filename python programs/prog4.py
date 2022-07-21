# addition of two numbers
first=input("enter first number")
second=input("enter second number")
sum=first +second #wrong way of doing we need to declare int so that compiler dont interpret it as a string
print(sum)
sum=int(first)+int(second)
print("the sum is :" + str(sum) )