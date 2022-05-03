# Copy() method is used to copy all the elements of a list to another list.
# When we copy a list a separate copy of all the elements is stored in another list. Both the list are independent.
# a = [10, 20, 30, 40]
# b = a.copy()
# Modification in a will not affect in b and vice versa
# 1
a = [10, 20, 30, 40, 50]
b = a.copy()
print("A:", a)
print("B:", b)

print()
print("Modifying A")
a[1] = 55
print("A:", a)
print("B:", b)

print()
print("Modifying A")
b[2] = 66
print("A:", a)
print("B:", b)


###########################################################################################################
# cloning list: We can clone a list into another list using slicing.
# When we clone a list a separate copy of all the elements is stored in another list. Both the list are independent.
# a = [10, 20, 30, 40]
# b = a[:]
# Modification in a will not affect in b and vice versa

a = [10, 20, 30, 40, 50]
b = a[:]
print("A:", a)
print("B:", b)

print()
print("Modifying A")
a[1] = 55
print("A:", a)
print("B:", b)

print()
print("Modifying A")
b[2] = 66
print("A:", a)
print("B:", b)


