a = {10,20, "Edward", 40}
print("Original Set:", a)
print(id(a))
print()
a.remove("Edward")
print("After Removing Set:", a)
print(id(a))
##########################
# 2
a = {10, 20, "Edward", 40}
print("Original Set:", a)
print(id(a))
print()
a.discard("Edward")
print("After Discard Set:", a)
print(id(a))