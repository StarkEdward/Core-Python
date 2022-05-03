for i in range(2):
    print("Outer Loop", i)
    for j in range(3):
        print("Innter Loop", j)
print("Rest of the Code")

# for i in range(1,5):
#     for j in range(1, i+1):
#         print(j, end = "")
#     print()

l1 = [1, 2, 3]
l2 = ["Sagar", "Sonu", "Vikki"]
for i in range(len(l1)):
    print(l1[i])
    for j in range(len(l2)):
        print(l2[j])