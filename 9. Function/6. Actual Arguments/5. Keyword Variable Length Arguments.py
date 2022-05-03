# Keyword Variable Length Arguments
#  1
def add(**num):
    z = num['a'] + num['b'] + num['c']
    print(z)
    print(num)
add(a = 5, b = 6, c = 12)
############################
# 2
def add(**num):
    z = num['a'] + num['b'] + num['c']
    print(z)
    print(num)
add(a = 5, b = 6, c = 12, d = 22)
###############################################
# 3
def add(x, **num):
    z = x +num['a'] + num['b'] + num['c']
    print(z)
    print(num)
add(5, a = 5, b = 6, c = 12)