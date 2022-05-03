# 1
a = {}

n = int(input("Number of Element you want: "))

for i in range(n):
    key = input("Enter key: ")
    val = input("Enter value: ")
    a.update({key:val})
print(a)

