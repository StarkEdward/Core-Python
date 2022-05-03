# You can delete entire tuple but not an element of tuple.
#
# 1
# a = (10, 20, 50, 21.3, "Edward")
# print(a)
# del a
# print(a)
############
# 2
a = (10, 20, -50, 21.3, "Edward")
print(a)

s1 = a[0:2]
s2 = a[3:]
tup = s1 + s2
print(tup)












