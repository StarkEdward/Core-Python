# 1
from numpy import *
n = int(input("Enter Number of Elements: "))
a = zeros(n, dtype= int)
print(a)
######################
# 2
from numpy import *
n = int(input("Enter Number of Elements: "))
a = zeros(n, dtype= int)
a[0] = 10
a[1] = 20
print(a)
################
# 3 Using for loop
from numpy import *
n = int(input("Enter number of Elements: "))
a = zeros(n, dtype=int)
for i in range(len(a)):
    x = int(input("Enter Element: "))
    a[i] = x
print(a)
# to get access for array element
for i in range(len(a)):
    print(a[i])
#############################
