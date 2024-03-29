# A tuple within another tuple is called as nested tuple or nesting of a tuple.
# Ex:- a =  (10, 20, 30,(50, 60))
#  b =(50, 60)
#  a = (10, 20, 30, b)
#  a = ( (10, 20, 30),(40, 50, 60) )
# a = ( (10, 20, 30),
#       (40, 50, 60)
#############################################################
# index:
# a = (10, 20, 30, (50, 60))                  |  10  |   20  |   30  |   |50|60| |
# b = (50, 60)                                                       |   [0] [1] |
# a = (10, 20, 30, b)                           [0]     [1]     [2]         [3]
#
#
#
# a = ( (10, 20, 30), (40, 50, 60))                   0       1       2
# a = ((10, 20, 30),                          0  |   10  |   20  |   30  |
#      (40, 50, 60))                          1  |   40  |   50  |   60  |
###################################################################################################
# Accessing Nested tuple
# a = (10, 20, 30, (50, 60))               #   |  10  |   20  |   30  |   |50|60| |
# b = (50, 60)                            #                           |   [0] [1] |
# a = (10, 20, 30, b)                     #      [0]     [1]     [2]        [3]
# print(a)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[3][0])
# print(a[3][1])
##################################
# 2
a = ( (10, 20, 30), (40, 50, 60))      #             0       1       2
# a = ((10, 20, 30),                      #    0  |   10  |   20  |   30  |
#      (40, 50, 60))                       #   1  |   40  |   50  |   60  |
# print(a)
# print("a[0]", a[0])
# print("a[1]", a[1])
# print(a[0][0])
# print(a[0][1])
# print(a[0][2])
# print(a[1][0])
# print(a[1][1])
# print(a[1][2])
#########################################################################################



