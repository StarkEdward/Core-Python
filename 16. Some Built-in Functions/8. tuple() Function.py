'''
Rather than being a function, tuple is actually an immutable sequence type.
This can be also used in type casting to convert iterable to tuple.
Syntax: tuple(iterable)
'''
# tuple() function
a = [10, 20, 30]
print(a)
print(type(a))
new_a = tuple(a)
print(new_a)
print(type(new_a))
print()

b = {10, 20, 30}
print(b)
print(type(b))
new_b = tuple(b)
print(new_b)
print(type(new_b))
print()

c = "Edward"
print(c)
print(type(c))
new_c = tuple(c)
print(new_c)
print(type(new_c))
print()

d = {101: "Edward", 102:"Jarvis", 103: "Buddha"}
print(d)
print(type(d))
new_d = tuple(d)
print(new_d)
print(type(new_d))
print()
