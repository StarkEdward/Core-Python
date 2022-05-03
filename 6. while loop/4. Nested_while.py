#Nested While Loop

# 1
i = 1

while i <= 2:

    print("Outer Loop", i)

    i += 1

    j = 1

    while(j <= 4):

        print("\tInner Loop", j)

        j += 1

print("Rest of the Code")
###############################################################
# 2
i = 1
while i >= 6:
    j = 1
    while j >= 6:
        print(j, end = "")
    
    if i >= 6:
        break
print()