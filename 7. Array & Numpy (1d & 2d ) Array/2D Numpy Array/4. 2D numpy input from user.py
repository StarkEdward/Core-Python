# using for loop
from numpy import *
r = int(input("Enter Number of rows: "))
c = int(input("Enter Number of Columns: "))
a = zeros((r, c), dtype= int)
print(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        x = int(input("Enter Elements: "))
        a[i][j] = x
print(a)
# display elements
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])
######################################
# user input using while loop
from numpy import *
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
a = zeros((r, c), dtype=int)
print(a)
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        x = int(input("Enter Element: "))
        a[i][j] = x
        j += 1
    i += 1
print(a)
# display elements
k = 0
while k < len(a):
    l = 0
    while l < len(a[k]):
        print(a[k][l])
        l += 1
    k += 1