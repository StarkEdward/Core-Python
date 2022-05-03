# Tuple: A tuple contains a group of elements which can be same or different types.
# Tuples are immutable.
# It is similar to List but Tuples are read-only which means we can not modify it's element.
# Tuples are used to store data which should not be modified.
# It occupies less memory compare to list.
# Tuples are represented using parentheses ().
# Ex: a = (10, 20, -50, 21.3, "Edward")
#################################################################
# Creating Empty Tuple
# Syntax\: tuple_name = ()
# Ex: a = ()

########################
# Creating Tuple
# We can create tuple by writing elements separated by commas inside parentheses
# with one element:
# b = ()   <----------- It will become integer.
# c = (10,)

# with Multiple Elements
# d = (10, 20, 30, 40)
# e = (10, 20, -50, 21.3, "Edward")
# f = 10, 20, -50, 21.3, "Edward"
##############################################################################
# Index: An index represents the position number of an tuple's element. The index start from 0 on wards and written inside square braces.
# Ex:- a = (10, 20, -50, 21.3, "Edward")
"""
                [0] =   10                      [-5] =   10
                [1] =   20                      [-5] =   20
     a =        [2] =   -50              a =    [-5] =   -50
                [3] =   21.3                    [-5] =   21.3
                [4] =   Edward                  [-5] =   Edward

"""
#######################################################################################
# Accessing Tuple's Element
a = (10, 20, -50, 21.3, "Edward")
"""
                   a[-5]     a[-4]      a[-3]    a[-2]       a[-5]
                |   10  |   20    |   -50    |  21.3     |   Edward   |
                   a[0]     a[1]      a[2]      a[3]          a[4]
                   
"""
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print()
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])
######################################################
# 1
b = (10,)
print(b, type(b))
#########
# 2
c = (10, 20, -50, 21.3, "Edward")
print(c, type(c))
###################
# 3
d = 11, 22, 33, "Edward"
print(d, type(d))
########
# 4

