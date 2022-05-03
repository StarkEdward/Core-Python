# one() 2D array
# 1
from numpy import *
a = ones((3,2))
print(a)
########################
# 2
from numpy import *
a = ones((3,2), dtype= int)
print(a)
#############################
# 3 indexing
from numpy import *
a = ones((3,2), dtype= int)
print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])
print(a[2][0])
print(a[2][1])
###################################
# 4 for loop without index
from numpy import *
a = ones((3, 2), dtype= int)
for i in a:
    for j in i:
        print(j)
    print()
#######################################
# 5 for loop with index
from numpy import *
a = ones((3,2), dtype= int)

for i in range(len(a)):
    for j in range(len(a[i])):
        print("Index", i, j, "=", a[i][j])
    print()
###################################
# 6 while loop
from numpy import *
a = ones((3, 2), dtype= int)
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print('index', i, j, "=", a[i][j])
        j += 1
    i += 1
    print()
#########################
