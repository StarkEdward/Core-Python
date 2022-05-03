# This function returns the "identity " of an object.
'''
The identity number is an integer which is guaranteed to be unique and constant for this object during its lifetime.
Two ojects with non-overlapping lifetimes may have the same id() value.
CPython implementation detail - This is the address of the object in memory.
# syntax: id(object)
'''
# 1
a = 20
b = 30.23
c = 'Edward'
d = [10, 20, 30]
e = (10, 20, 30)
f = {10, 20, 30}
g = {101: "Edward", 102: "Jarvis", 103: "Manthan"}

# id () function
print(id(a))
print()
print(id(b))
print()
print(id(c))
print()
print(id(d))
print()
print(id(e))
print()
print(id(f))
print()
print(id(g))
print()

