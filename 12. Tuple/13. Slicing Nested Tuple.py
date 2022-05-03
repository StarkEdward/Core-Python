# Slicing Nested Tuple.
x = ((10, 20, 30),
     (40, 50, 60),
     (70, 80, 90),
     (11, 22, 33),
     (44, 55, 66),
     (77, 88, 99),
     (12, 13, 14))
print("Original Tuple")
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

print("From 0th Position to 4th Postion")
c = x[:5]
print(c)
print()

print("Last 4 Tuple")
d = x[-4:]
print(d)
print()

print("From 0th Position to 6th Position stepsize 2")
e = x[0:7:2]
print(e)
print()

print("From 0th position to last tuple with stepsize 3")
f = x[::3]
print(f)
print()

print("Last 6 Tuples with [-5-(-3)] = 2 Tuples towards right")
g = x[-5:-3]
print(g)
print()

print("********************************************************************")
print()
print("Slice Nested 2nd Position, 0th Position")
h = x[2:3]
print(h)
i = x[2:3][0]
print(i)
print()

print("Slice 2nd Tuple & Extract Elements")
# Extraction only one element
j = x[2:3][0][0]
print(j)
# Extracting all elements using loop
k = x[2:3][0]
for ele in k:
     print(ele)
print()

print("Last Nested 4 Tuple then 1st Position then Extract elements.")
l = x[-4:]
print(l)
m = x[-4:][1]
print(m)
print()

#Extract only one element
p = x[-4:][1][0]
print(p)

# Extract all elements
q = x[-4:][1]
for ele in q:
     print(ele)
