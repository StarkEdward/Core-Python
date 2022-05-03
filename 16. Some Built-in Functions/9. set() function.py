'''
This function returns a new set object, optionally with elements taken from iterable.
This can be also used in type casting to convert iterable to set.
Syntax: set(iterable)
'''
# set() Function
a = [10, 20, 30]
print(a)
print(type(a))
new_a = set(a)
print(new_a)
print(type(new_a))
print()

b = (10, 20, 30)
print(b)
print(type(b))
new_b = set(b)
print(new_b)
print(type(new_b))
print()

c = "Edward"
print(c)
print(type(c))
new_c = set(c)
print(new_c)
print(type(new_c))
print()

d = {101: "Edward", 102:"Jarvis", 103: "Buddha"}
print(d)
print(type(d))
new_d = set(d)
print(new_d)
print(type(new_d))
print()


