# import numpy
# a = numpy.array([[10, 20, 30, 40],
#             [50, 60, 70, 80]])
# print(a)
#############################
# import numpy
# a = numpy.array([[10, 20, 30, 40],
#             [50, 60, 70, 80]])
# print(a[0][0])
# print(a[0][1])
# print(a[0][2])
# print(a[0][3])
# print(a[1][0])
# print(a[1][1])
# print(a[1][2])
# print(a[1][3])
##################################
# import numpy
# a = numpy.array([[10, 20, 30, 40],
#             [50, 60, 70, 80]], dtype=float)
# print(a[0][0])
# print(a[0][1])
# print(a[0][2])
# print(a[0][3])
# print(a[1][0])
# print(a[1][1])
# print(a[1][2])
# print(a[1][3])
####################################
# import numpy
# a = numpy.array([[10, 20, 30, 40],
#             [50, 60, 70, 80.2]], dtype=float)
# print(a.dtype)
# print(a[0][0])
# print(a[0][1])
# print(a[0][2])
# print(a[0][3])
# print(a[1][0])
# print(a[1][1])
# print(a[1][2])
# print(a[1][3])
#############################
# from numpy import *
# a = array([['Sagar', 'Sonu', 'Golu', 'Chetan'],
#             ['Stark', 'Edward', 'Jarvis', 'Buddha']], dtype=str)
# print(a.dtype)
# print(a[0][1])
# print(a[0][2])
# print(a[0][3])
# print(a[1][0])
# print(a[1][1])
# print(a[1][2])
# print(a[1][3])
###########################
# modifying 2d Array
# from numpy import *
# a = array([[10, 20, 30, 40],
#            [50, 60, 70, 80]])
# a[0][1] = 45
# a[1][2] = 100
# print(a[0][1])
# print(a[1][2])
#####################################
# for loop without index
# from numpy import *
# a = array([[10, 20, 30, 40,],
#            [50, 60, 70, 80]])
# for r in a:
#     for k in r:
#         print(k)
#     print()
######################################
# for loop with index
# from numpy import *
# a = array([[10, 20, 30, 40],
#            [50, 60, 70, 80]])
# a[1][2] = 123
# n = len(a)
# for i in range(n):
#     for j in range(len(a[i])):
#         print(a[i][j])
#     print()
##############################
# While loop
from numpy import *
a = array([[10, 20, 30, 40],
           [50, 60, 70, 80]])
n = len(a)
i = 0
while i < n:
    j = 0
    while j < len(a[i]):
        print("Index", i, j, "=", a[i][j])
        j += 1
    i += 1
    print()
#######################################
