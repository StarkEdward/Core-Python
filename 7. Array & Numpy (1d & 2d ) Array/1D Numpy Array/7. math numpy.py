# Adding in array
from numpy import *
a = array([101, 102, 103, 104, 105])
a = a + 5
print(a)
# or
for i in range(len(a)):
    print(a[i])
#################
# Subtractin of array
from numpy import *
a = array([101, 102, 103, 104, 105])
a = a - 5
print(a)
# or
for i in range(len(a)):
    print(a[i])
############################
#
from numpy import *
a = array([101, 102, 103, 104, 105])
a = a * 5
print(a)
# or
for i in range(len(a)):
    print(a[i])
###############################
#
from numpy import *
a = array([101, 102, 103, 104, 105])
a = a / 5
print(a)
# or
for i in range(len(a)):
    print(a[i])
##########################
#
from numpy import *
a = array([101, 102, 103, 104, 105])
a = a % 5
print(a)
# or
for i in range(len(a)):
    print(a[i])
##################################
#
from numpy import *
a = array([101, 102, 103, 104, 105])
b = array([10, 25, 13, 12, 22])
c = a + b
print(c)
# or
for i in c:
    print(i)