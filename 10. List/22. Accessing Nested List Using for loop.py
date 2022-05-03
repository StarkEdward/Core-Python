# 1
a = [10, 20, 30, [50, 60]]
for i in a:
    print(i)
##############################
# 2
a = [10, 20, 30, [50, 60]]
n = len(a)
for i in range(n):
    if type(a[i]) is list:
        if len(a[i])>1:
            m = len(a[i])
            for j in range(m):
                print(i, j, a[i][j])

    else:
        print(i, a[i])
############
# 3
a = [[10, 20, 30], [40, 50, 60]]
# without index
for r in a:
    for c in r:
        print(c)
    print()
##################
# 4 with index

a = [[10, 20, 30], [40, 50, 60]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(i, j, a[i][j])
    print()



