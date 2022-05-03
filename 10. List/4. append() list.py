# append() list
# 1
a = [10, 20, -60, 21.3, "Edward"]
a.append(44)
a.append("Jarvis")
print(a)
###########################
# 2
a = [10, 20, -50, 21.3, "Edward"]
print("Before appending:")
for ele in a:
    print(ele)

# appending an element
a.append(100)
print("After Appending:")
for ele in a:
    print(ele)