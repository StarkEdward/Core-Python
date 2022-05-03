# This method returns te value of the specified key.
# if key is not found then it inserts key with the specified value.
# syntax:- dict_name.setdefault(key,value)

# 1
stu = {101:"Edward", 102:"Stark", 103:"Jarvis"}
print("Original Dict:")
print(stu)
print()

returned_val = stu.setdefault(109, 'Python')
print("After SetDefault Dict:")
print(stu)
print("Returned value:", returned_val)
print()


