# Access tuple using for loop
# 1 without using index
a = (10, 20, 30, "Edward" )
for ele in a:
    print(ele)
############################
# 2 using index
a = (10, 20, 30, "Edward")
for i in range(len(a)):
    print("Index", i, "=", a[i])
################