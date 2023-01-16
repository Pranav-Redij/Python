#i am going to make recursive function so that 
#function calling will be known

def factorial(n):
    if(n==0 or n==1):#in python or(||),and(&&)
        return 1
    #elif:(this is same as else if)
    else:
        return n*factorial(n-1)

n=int(input("enter the number for finding factorial:"))
print("factorial of ",n," is:",factorial(n))
