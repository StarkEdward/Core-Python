# 1
a = []
n = int(input("Enter Number of elements you want in list: "))
for i in range(n):
    a.append(input(f"Enter {i} element: "))

for ele in a:
    print(ele)
####################
# 2 Getting Integer value input in list
a = []
n = int(input("Enter number of elements: "))
for i in range(n):
    a.append(int(input(f"Enter {i} element: ")))

print("list:", a)
for ele in a:
    print(ele)

