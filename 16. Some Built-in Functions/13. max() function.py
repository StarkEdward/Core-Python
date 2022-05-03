'''
This function returns the largest item in an iterable or the largest of two or more arguments.
If one positional argument is provided, it should be an iterable. 
The largest item in the iterable.
If two or more positional arguments are provided, the largest of the positional arguments is returned.
synatx:- 
max(iterable)
max(arg1, arg2, ...)
'''
# 1
b = [10, 20, 30, 40, 5]
c = (10, 20, 30, 4, 60)
d = {10, 9, 62, 45, 20}
e = {101:'Edward', 102 : "Jarvis", 103: "Stark", 2: "sonu"}
f = [[10,20], [30,40], [50,60], [2, 5]]
g = [(101, "Edward"), (102, "Jarvis"), (2, "Sonu"), (103, "Stark")]

print(max(b))
print(max(c))
print(max(d))
print(max(e))
print(max(f))
print(max(g))

a = max(10, 20, 3)
print(a)