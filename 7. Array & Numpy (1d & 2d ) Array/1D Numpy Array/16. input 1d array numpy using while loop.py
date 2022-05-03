from numpy import *
n = int(input("Enter Number of Elements: "))
a = zeros(n, dtype=int)
u = len(a)
i = 0
j = 0
while i < u:
    x = int(input("Enter Element: "))
    a[i] = x
    i += 1
print(a)
# accessing array
while j < u:
    print(a[j])
    j += 1