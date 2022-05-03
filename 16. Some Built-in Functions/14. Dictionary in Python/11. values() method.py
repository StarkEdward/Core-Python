
# this method returns a sequence of values from the dictionary.
# syntax:- dict_name.values()

#1
stu = {101:"Edward", 102:"Stark", 103:"Jarvis"}
print("Original Dict:")
print(stu)
print()

all_val = stu.values()
print(all_val)
print(type(all_val))
print()

lst_val = list(all_val)
print(lst_val)
print()

for val in lst_val:
    print(val)



