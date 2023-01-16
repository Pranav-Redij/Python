#loops and condition
#if True:
#    print('condition is true')
city='Mumbai'
if city=='Mumbai':
    print('city is Mumbai')
elif city=='banglore':#elif is like else if() of cpp
    print('city is banglore')
else:
    print('city was not matched')

print(' ')

#and--&&
#or--||
#not--~
user='pranav'
if user=='pranav' and False:
    print("welcome!")
else:
    print("you're at wrong place ;)")

#conditional operators
# ==
# !=
# <
# <=
# >
# >=
# is (used for object comparisons)(if id is same then return true or return false)

#python generate unique id for every thing 
#eg.print(id(user))

####/\/\//\//\//\/\//\/\/\/\/\/\/\\//\/\//\/\/\\/\/\/\///\/\\/\/\\/\
#looping
nums=[1,2,3,4,5]
for x in nums:
    print(x)

for num in nums:
    if(num==3):
        print('found!!')
        break
    print(num)



#while loop

i=0
while i<10:
    print(i)
    i+=1