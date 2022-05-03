# Slicing Nested List.
x = [[10, 20, 30],
     [40, 50, 60],
     [70, 80, 90],
     [11, 22, 33],
     [44, 55, 66],
     [77, 88, 99],
     [12, 13, 14]]
print("Original List")
print(x)
print()

print("From 1st Position to 4th Position")
a = x[1:5]
print(a)
print()

print("From 0th Position to last Position")
b = x[0:]
print(b)
print()

print("From 0th Position to 4 th Position")
c = x[:4]
print(c)
print()

print("Last 4 list")
d = x[-4:]
print(d)
print()

print("From 0th Position to 6th Position stepsize 2")
e = x[0:7:2]
print(e)
print()

print("From 0th Position to last with stepsize 3")
f = x[::3]
print(f)
print()

print("Last 5 list with [-5-(-3)]=2 list toward right")
g = x[-5:-3]
print(g)
print()
print("***********************************************************************")
print()
#######################
print("Slilce Nested 2nd position, 0th postion")
m = x[2:3]
print(m)
n = x[2:3][0]
print(n)
print()

print("Slice 2nd list the extract elements")
# Extracitn only one element
j = x[2:3][0][0]
print(j)
# Extracting all elements
i = x[2:3][0]
for ele in i:
     print(ele)
print()
##################################
print("Last Nested 4 list then 1st position then extract elements")
k = x[-4:][:]
print(k)
l = x[-4:][1]
print(l)
print()

# Extracting only one element
s = x[-4:][1][0]
print(s)
# Extracting all elements
i = x[-4:][1]
for ele in i:
     print(ele)
print()
#################################################################
