'''
This function creates a new dictionary. This can be also used in type casting to convert iterable to dict.
Syntax: dict(**kwarg)
'''
# dict() function
a = [(101, "Edward"), (102, "Jarvis"), (103, "Shrikant")]
print(a)
print(type(a))
new_a = dict(a)
print(new_a)
print(type(new_a))
print()

b = ((101, "Edward"), (102, "Jarvis"), (103, "Shrikant"))
print(b)
print(type(b))
new_b = dict(b)
print(new_b)
print(type(new_b))
print()

c = ([101, "Edward"], [102, "Jarvis"], [103, "Shrikant"])
print(c)
print(type(c))
new_c = dict(c)
print(new_c)
print(type(new_c))
print()