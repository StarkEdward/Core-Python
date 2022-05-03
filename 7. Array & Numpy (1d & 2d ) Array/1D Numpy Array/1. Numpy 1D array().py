# Numpy
# To check version of numpy
# import numpy
# print(numpy.__version__)
######################

# One Demensional Array using array() function
# 1
# import numpy
# roll = numpy.array([101, 102, 103, 104, 105])
# print(roll)
# print(roll.dtype)   # to check datatype of array
# print(roll[0])
# print(roll[1])
# print(roll[2])
# print(roll[3])
# print(roll[4])

#####################################
# 2 # Explecitly converting to float
# import numpy
# roll = numpy.array([101, 102, 103, 104, 105], dtype = float)
# print(roll)
# print(roll.dtype)   # to check datatype of array
# print(roll[0])
# print(roll[1])
# print(roll[2])
# print(roll[3])
# print(roll[4])
##################################
# 3 Implicit conversion to float
import numpy
# roll = numpy.array([101, 102, 103, 104, 10.5])
# print(roll)
# print(roll.dtype)   # to check datatype of array
# print(roll[0])
# print(roll[1])
# print(roll[2])
# print(roll[3])
# print(roll[4])
############################################
# 4 Unicode 1 Character or string.
# import numpy
# roll = numpy.array(['A', 'B', 'C', 'D', 'E'])
# print(roll)
# print(roll.dtype)   # to check datatype of array
# print(roll[0])
# print(roll[1])
# print(roll[2])
# print(roll[3])
# print(roll[4])
####################################
# 5 String
# import numpy
# roll = numpy.array(['Sonu', 'Sagar', 'Edward', 'Stark', 'Jarvis'])
# print(roll)
# print(roll.dtype)   # to check datatype of array
# print(roll[0])
# print(roll[1])
# print(roll[2])
# print(roll[3])
# print(roll[4])
#############################################
# Modifying one Dimensional array
# from numpy import *
# roll = array([101, 102, 103, 104, 105])
# print(roll.dtype)
# print("Before Modify: ", roll)
# # Modifying
# roll[1] = 110
# roll[2] = 222
# print("After Modify: ", roll)
#################################################
# for loop in one Dimensional Array
# 1 Without using index
# from numpy import *
# roll = array([101,102,103,104,105])
# for i in roll:
#     print(i)

# 2 Using index
# from numpy import *
# roll = array([101, 102, 103, 104, 105])
# n = len(roll)
# for i in range(n):
#     print(i, "=", roll[i])
###############################################

# using while loop in One Dimensional array
# 1
from numpy import *
roll = array([101, 102, 103, 104, 105])
n = len(roll)
i = 0
while i < n:
    print(roll[i])
    i += 1

# 2 modifying some elements
from numpy  import *
roll = array([101, 102, 103, 104, 105])
roll[1] = 111
roll[3] = 333
i = 0
while i < len(roll):
    print("index", i, " = ", roll[i])
    i += 1



