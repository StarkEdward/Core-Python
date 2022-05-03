# arange()

# 1
from numpy import *
a = arange(5)
print(a)
#########################
from numpy import *
a = arange(5.0)
print(a)
###########################
# 3
from numpy import *
a = arange(1, 6)
print(a)
###############################
# 4
from numpy import *
a = arange(1, 10, 2)
print(a)
################################
# 5
from numpy import *
a = arange(1,6)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
###############################
# for loop
# 6 without index
from numpy import *
a = arange(1,6)
for ele in a:
    print(ele)
##################################
# 7 with index
from numpy import *
a = arange(1, 6)
for i in range(len(a)):
    print("Index", i, "=", a[i])
##################################
# 8 while loop
from numpy import *
a = arange(1,6)
i = 0
while i < len(a):
    print("Index", i, "=", a[i])
    i += 1
################################
