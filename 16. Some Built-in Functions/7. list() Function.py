'''
Rather than being a function, list is actually a mutable sequence type. This can be used in type casting to convert iterable to list.
Syntax: list(iterable)
'''
# list() function
a = (10, 20, 30)
print(a)
print(type(a))
new_a = list(a)
print(new_a)
print(type(new_a))
print()

b = {10, 20, 30}
print(b)
print(type(b))
new_b = list(b)
print(new_b)
print(type(new_b))
print()

c = "Edward"
print(c)
print(type(c))
new_c = list(c)
print(new_c)
print(type(new_c))
print()

d = {101: "Edward", 102:"Jarvis", 103: "Buddha"}
print(d)
print(type(d))
new_d = list(d)
print(new_d)
print(type(new_d))
print()