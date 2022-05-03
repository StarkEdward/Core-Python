'''
This function returns the size of an object in bytes.
The object can be any getsizeof of object.
All built-in objects will return correct results, but this does not have to hold true for third-party extension as it is implementation specific.
Only the memory consumption directly attributed to the object is accounted for , not the memory consumption of objects it refers to.
This is part of sys module so you have to import sys module before using this functin.
# Syntax:
from sys import *
getsizeof(object)
'''
# 1
from sys import getsizeof
a = 20
b = 30.23
c = 'Edward'
d = [10, 20, 30]
e = (10, 20, 30)
f = {10, 20, 30}
g = {101: "Edward", 102: "Jarvis", 103: "Manthan"}

# getsizeof () function
print(getsizeof(a))
print()
print(getsizeof(b))
print()
print(getsizeof(c))
print()
print(getsizeof(d))
print()
print(getsizeof(e))
print()
print(getsizeof(f))
print()
print(getsizeof(g))
print()