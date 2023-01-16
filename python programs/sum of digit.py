#sum of digit program 
n=int(input("enter the number:"))
ans=0
while n>0:
    ans+=n%10
    #n/=10 (this will return ans in form of floating)
    n//=10 #(this is same as n=int(n/10) )

print("sum of digit is:",ans)
