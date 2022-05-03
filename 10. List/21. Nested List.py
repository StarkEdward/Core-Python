# 1
a = [10, 20, 30, [50, 60]]
print(a[0])
print(a[1])
print(a[2])
print(a[3][0])
print(a[3][1])
print(a)
##########################
# 2
a = [[10, 20, 30],
     [40, 50, 60]]
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[1][0])
print(a[1][1])
print(a[1][2])
print(a)
##########################
# Modifying Nested list.
# 1
b = [50, 60]
a = [10, 20, 30, b]
print("Before Modifying:", a)
a[1] = 100
a[3][0] = 5
print("After Modifying:", a)
####################
# 2
a = [[10, 20, 30],
     [40, 50, 60]]
print("Before Modifying:", a)
a[0][1] = 2
a[1][2] = 6
print("After Modifying:", a)
##################################


















