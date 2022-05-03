# ones()
# 1
from numpy import *
a = ones(5)
print(a)
#####################
# 2
from numpy import *
a = ones(5, dtype=int)
print(a)
############################
# 3
from numpy import *
a = ones(5)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
###########################
# 4 using for loop without index
from numpy import *
a = ones(5)
for ele in a:
    print(ele)
#####################
# 5 for loop with index
from numpy import *
a = ones(5)
for i in range(len(a)):
    print("Index", i, "=", a[i])
######################################
# 6 while loop
from numpy import *
a = ones(5)
i = 0
while i < len(a):
    print("Index", i, "=", a[i])
    i += 1
#####################################
