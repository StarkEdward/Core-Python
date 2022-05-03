# Tuples are immutable so it is not possible to modify, update or delete its element.
a = (10, 20, -50, 21.3, "Edward")
print(a, id(a))
b = (40, 50)
print(b, id(b))
tup1 = a + b
print(tup1, id(tup1))
###############
# 2
a = (10, 20, -50, 21.3, "Edward")
print(a)
tup2 = a[0:3]
print(tup2)
##################
# 3
a = (10, 20, -50, 21.3, "Edward")
print(a)

c = (101, 102)
s1 = a[0:2]
s2 = a[3:]
tup3 = s1 + c + s2
print(tup3)

