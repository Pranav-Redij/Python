#Dictionary are key-value pair,like hash_map in java , unordered_map in cpp 
# syntax = dic_name = {key:value}
student={'pranav':21,'akshaya':26}
print(student)
#print(student['pranav'])
#if one key was not present but still wanted to find that out 
#then it will give error to us
#so if we dont want error then do this 

print(student.get('pranav'));
print(student.get('name','not_found'));
 
#trying to assign value and key
student['name']=111;
print(student)

#in pop only value will return not key 

