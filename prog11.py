#sorting 
list=[0,2,5,3,7,6]
#sorting function
sorted_list=sorted(list)
print(sorted_list)
#sorting method(inplace sorting means sort the original list)
list.sort()

#difference between function and method
#method need instance of class means need object and function doesnt need that 

#if we have negative inside the list we wanted to sort based on the absolute values then 
#sorted_list=sorted(list,key=abs)