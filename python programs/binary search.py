#binary search using python

#creating empty list
ls=[]
#indexing is start from 0 to n-1 just like array in cpp

#creating size of list
n=int(input("enter the size of list:"))

#for loop here is bit different 
for i in range(0,n):
    ele=int(input())
    ls.append(ele)#appending the element

#now taking input is done now starting the binary search algo
find=int(input("enter the element to find inside the list"))
s=0
e=n-1
while s<e:
    mid=int((s+e)/2)#we have to type cast it since it will return float value
    if(ls[mid]==find):
        print("found!!!!")
        break
    elif (ls[mid]<find):
        s+=1
    elif ls[mid]>find:
        e-=1


