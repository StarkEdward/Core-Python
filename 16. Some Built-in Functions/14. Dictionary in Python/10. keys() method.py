# keys() method: This method returns a sequence of keys from the dictionary
# syntax dixt_name.keys()

#1
stu = {101:"Edward", 102:"Stark", 103:"Jarvis"}
print("Original Dict:")
print(stu)
print()

all_keys = stu.keys()
print(all_keys)
print(type(all_keys))

lst = list(all_keys)
print(lst)
print()

for i in lst:
    print(i)




