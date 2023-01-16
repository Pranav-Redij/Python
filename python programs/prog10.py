#list slicing
#index are like 0 1 2
#              -3 -2 -1
my_list=[0,1,2]
print(my_list[0])
print(my_list[0:2])
print(my_list[-3:-1])
print(my_list[0:])#from 0 to last ,,and same if we did with first index

#if we try to print from right to left then it will throw error

#but if we wanted to traverse in reverse order then what?
#my_list[start:end:step]
#step will tell us that iternate with step 
print(my_list[-1:-3:-1])

#same slicing can be done on string also
