# Logical Operator

# Logical and
a = 5
b = 2
c = 3
d = 15
print(a>b and a>c)
print(a>b and a<c)
print(a<b and a>c)
print(a<b and a<c)
print(a>b and c)
print(a<b and c)

print(a>b and c and d)
print(a<b and c and d)

# Logical or
a = 5
b = 2
c = 3
d = 15

print(a>b or a>c)
print(a>b or a<c)
print(a<b or a>c)
print(a<b or a<c)
print(a>b or c)
print(a<b or c)

print(a>b or c or d)
print(a<b or c or d)

# Logical not
a = 5
b = 2

print(not(a>b))
print(not(a<b))