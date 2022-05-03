'''
This function returns an integer object or return 0  if no arguments are given.
Syntax: int(a)
'''
# 1 int() function
a = 10.56
print('Flaot:', a)
print(type(a))
new_a = int(a)
print("int:", new_a)
print(type(new_a))
print()

b = '10'
print("String:", b)
print(type(b))
new_b = int(b)
print("int:", new_b)
print(type(new_b))
print()

# Below code will show error
c = "Edward"
print("String:", c)
print(type(c))
new_c = int(c)
print("int:", new_c)
print(type(new_c))
print()