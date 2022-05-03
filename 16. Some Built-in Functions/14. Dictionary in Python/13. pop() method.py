# this method is used to remove the item with specified key.
# it returns the removed item's value.
# if key is not found then the default value is returned.
# if key is not found and default value is not given then shows KeyError

# syntax: dict_name.pop(key, default value)
#
# 1
stu = {101:"Edward", 102:"Stark", 103:"Jarvis"}
print("Original Dict:")
print(stu)
print()
#
removed_val = stu.pop(101)
print("After Removing Dict:")
print(stu)
print("Removed value:", removed_val)
print()
###############
# 2
stu = {101:"Edward", 102:"Stark", 103:"Jarvis"}
print("Original Dict:")
print(stu)
print()

removed_val = stu.pop(104, "Not Found")
print("After Removing Dict:")
print(stu)
print("Removed value:", removed_val)
print()