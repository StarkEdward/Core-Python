#
from numpy import *
n = array([[10, 20, 30, 40],
           [50, 60, 70, 80],
           [90, 100, 110, 120]])
print(n)
print("Original Array")
print(n[0]) # first row
print(n[1]) # second row
print(n[2]) # thrid row

# print("0th Row all column")
a = n[0, : ]
print(a)
#
# print("1th Row all column")
a = n[1, : ]
print(a)
#
# print("2nd Row all column")
a = n[2, : ]
print(a)

# print("all row and all column")
a = n[: , : ]
print(a)

# 0th Column and all rows
a = n[: , 0]
print(a)
for i in a:
    print(i)
# 1st Column and all rows
a = n[: , 1]
print(a)
# 2nd Column and all rows
a = n[: , 2]
print(a)
# 3rd Column and all rows
a = n[: , 3]
print(a)

a = n[0:1, 0:1]
print(a)
#
a = n[2:3, 3:4]
print(a)

a = n[0:2, 1:5]
print(a)

a = n[1:3, 0:4:2]
print(a)

