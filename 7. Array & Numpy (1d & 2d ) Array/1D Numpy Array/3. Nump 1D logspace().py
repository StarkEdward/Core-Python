# logspace() function
# 1
from numpy import *
a = logspace(1,3)
print(a)
###########################
# 2
from numpy import *
a = logspace(1, 3, 5)
print(a)
#########################
# 3
from numpy import  *
a = logspace(1, 3, 5, base= 12.0)
print(a)
############################
# 4
from numpy import *
a = logspace(1, 3, 5, endpoint= False, base= 2)
print(a)
############################
# 5
from numpy import *
a = logspace(1, 3, 5)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
###############################
# Using for loop
# 6 without index
from numpy import *
a = logspace(1, 3, 5)
for ele in a:
    print(ele)
# -----------------------
# 7 with index
from numpy import *
a = logspace(1, 3 ,5)
for i in range(len(a)):
    print("Index", i, "=", a[i])
######################################
# 8 While Loop
from numpy import *
a = logspace(1 ,3, 5)
i = 0
while i < len(a):
    print("Index", i, "=", a[i])
    i += 1
#####################################
