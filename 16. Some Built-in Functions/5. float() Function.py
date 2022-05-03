'''
This function returns an floating point number object.
# syntax: float(a)
'''
# float() Function
a = 10
print('Int:', a)
print(type(a))
new_a = float(a)
print("float:", new_a)
print(type(new_a))
print()

b = "10.56"
print("String:", b)
print(type(b))
new_b = float(b)
print("float:", new_b)
print(type(new_b))
print()

# Below code will show error
c = "Edward"
print("String:", c)
print(type(c))
new_c = float(c)
print("float:", new_c)
print(type(new_c))
print()