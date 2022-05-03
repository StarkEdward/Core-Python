# List of tuple:
"""
a = [10, 20, (30, 40)]
b = [(10, 20), (30, 40)]

"""
# 1
# a = [10, 20, (30, 40)]
# print("Original List A:", a)
# print("Id of A:", id(a))
# print("Type of A: ",type(a))
# print()

# Appending a new tuple
# a.append((50, 60))
# print("After Appending a tuple:", a)
# print("Id of A:", id(a))
# print("Type of A: ",type(a))
# print()

# Accessing List of Tuple using  for loop
# n = len(a)
# for i in range(n):
#     if type(a[i]) is tuple:
#         if len(a[i])> 1 :
#             m = len(a[i])
#             for j in range(m):
#                 print(i,j, a[i][j])
#     else:
#         print(i, a[i])
##############################
# 2 list of tuple
a = [(10, 20),(30, 40)]
print("Original List A:", a)
print("Id of A", id(a))
print()

# append in list of tuple
a.append((50, 60))
print("After Appending Tuple A: ", a)
print("Id of A", id(a))
print()

# Accessing List of tuple
for i in range(len(a)):
    for j in range(len(a[i])):
        print(i, j, a[i][j])
    print()
