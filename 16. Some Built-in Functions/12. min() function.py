'''
This function returns the smallest item in an iterable or the smallest of two or more argument.
If one positional argument is provided, it should be an iterable.
The smallest item in the iterable is returned.
If two or more positional arguments are provided, the smallest of the positional arguments is returned.
# syntax: min(iterable
min(arg1, arg2, ....)
'''
# 1
b = [10, 20, 30, 40, 5]
c = (10, 20, 30, 4, 60)
d = {10, 9, 62, 45, 20}
e = {101:'Edward', 102 : "Jarvis", 103: "Stark", 2: "sonu"}
f = [[10,20], [30,40], [50,60], [2, 5]]
g = [(101, "Edward"), (102, "Jarvis"), (2, "Sonu"), (103, "Stark")]

print(min(b))
print(min(c))
print(min(d))
print(min(e))
print(min(f))
print(min(g))


a = min(10, 20, 3)
print(a)