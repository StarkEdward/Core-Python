# Break Statement

for i in range(10):
    if (i == 5):
        break
    print(i)
print("Rest of the code")

for i in range(10):
    print(i)
    if (i == 5):
        break
print("Rest of the code")

# Continue Statement

for i in range(5):
    if (i == 3):
        continue
    print(i)
print("Rest of the code")

# Pass Statement

a = 10
b = 5
if a > b:
    pass
else:
    print("less")
print("rest of the code: Addition of a + b = ", a + b)
