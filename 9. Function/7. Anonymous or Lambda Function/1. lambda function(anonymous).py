# Anonymous function or lamda function

# 1
show = lambda x : print(x)
show(5)
######
# 2
add = lambda x, y : x + y
print(add(5, 4))
######
# 3
add_sub = lambda x, y : (x + y, y - x)
a, s = add_sub(5, 8)
print(a)
print(s)
#######
# 4
sub = lambda x, y = 3 : (x - y)
print(sub(5))