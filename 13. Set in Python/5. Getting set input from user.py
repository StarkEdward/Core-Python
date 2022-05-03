# Gettin input forom user
# 1
a = set()

n = int(input("Enter Number of Elements: "))

for i in range(n):
    el = input("Enter Element: ")
    a.add(el)

print(a)
for i in a:
    print(i)
