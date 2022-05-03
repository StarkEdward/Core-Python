# 1
x = [101, 102, 103, 104, 105, 106, 107]
print("Original List:", x)
for i in range(len(x)):
    print(i, "=", x[i])
print()

print("From 1st Position to 4th Position.")
a = x[1:5]
for i in a:
    print(i)
print()

print("From 0th Position to last Position.")
b = x[0:]
for i in b:
    print(i)
print()

print("From 0th Positin to 4th Postion")
c = x[:5]
for i in c:
    print(i)

print("From 3rd Position to last Position.")
d = x[3:]
for i in d:
    print(i)
print()

print("Last 4 Elements")
e = x[-4:]
for i in e:
    print(i)
print()

print("From 0th Position to last position with stepsize 2")
f = x[0::2]
for i in f:
    print(i)
print()

print("From 0th positon to 6th Position with stepsize 2")
g = x[0:7:2]
for i in g:
    print(i)
print()

print("Lst 5 Elements with [-5-(-3)] = 2 elements toward right")
h = x[-5:-3]
for i in h:
    print(i)
print()






