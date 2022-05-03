# return statement Single Value
# Defining a Function
def add(y):
    x = 10
    c = x + y
    return c
# calling a function
sum = add(20)
print(sum)
# ----------------------------------------------
# 2
def sub(y):
    x = 10
    c = y - x
    return c

print(sub(20))
# ----------------------------------------------
# 3 Return statement Multiple value
# Defining a Function
def add(y):
    x = 10
    c = x + y
    d = y - x
    return c, d, 50
# calling a function
# sum, sub, a = add(20)
# print(sum)
# print(sub)
# print(a)
print(add(20), type(add(20)))