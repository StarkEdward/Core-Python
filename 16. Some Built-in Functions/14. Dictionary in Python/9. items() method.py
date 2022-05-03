# items() method: This method returns an object that contains key-value pairs of dictionary.
# The pairs are stored as tuple in the object.
# syntax: dict_name.items()
##################################################
# 1
stu = {101:"Edward", 102:"Stark", 103:"Jarvis"}
print("Original Dict:")
print(stu)
print()

it = stu.items()
print(it)
print(type(it))

lst = list(it)
print(lst)
print()

print(lst[0])
print(lst[0][0])

for r in lst:
    for c in r:
        print(c)











