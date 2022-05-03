# Variable Length Arguments
# 1
def add(*num):
    z = num[0] + num[1] + num[2]
    print(z)
add(5, 2, 3,)
########################
# 2
def add(*num):
    z = num[0] + num[1] + num[2]
    print(z)
add(5, 2, 3, 4, 8, 9)
############################
# 3
def add (x, *num):
    z = x + num[0] + num[1]
    print(z)
add(5, 2, 4)