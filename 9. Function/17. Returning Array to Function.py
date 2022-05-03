# Returning Array to function
# from array import *
#
# def show(ar):
#     print("Passed Array Ar:", ar)
#     print(type(ar))
#     for i in ar:
#         print(i)
#     return ar
#
# a = array("i", [101, 102, 103])
# y = show(a)
# print("Returning Array Y:", y)
# print(type(y))
# for i in y:
#     print(i)
#######################
from array import *

def show():
    a = array("i", [101, 102, 103])
    return a


y = show()
print("Returning Array Y:", y)
print(type(y))
for i in y:
    print(i)






