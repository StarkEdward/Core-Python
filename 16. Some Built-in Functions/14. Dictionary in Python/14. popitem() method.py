# This mehtod is used to remove the item which was last inserted into the dictionary.
# It returns the removed item in the form of tuple, Pairs are returned in LIFO order.
# syntax: dict_name.popitem()
# 1
stu = {101:"Edward", 102:"Stark", 103:"Jarvis"}
print("Original Dict:")
print(stu)
print()

removed_item =  stu.popitem()
print("After Removing Dict:")
print(stu)
print("Removed Item:", removed_item)
print()






