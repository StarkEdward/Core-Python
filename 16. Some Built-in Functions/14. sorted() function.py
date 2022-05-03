'''
this function returns a new sorted list from the items in iterable.
# syntax: sorted(iterable)
'''
# 1
b = [10, 20, 30, 40, 5]
c = (10, 20, 30, 4, 60)
d = {10, 9, 62, 45, 20}
e = {101:'Edward', 102 : "Jarvis", 103: "Stark", 2: "sonu"}
f = [[10,20], [30,40], [50,60], [2, 5]]
g = [(101, "Edward"), (102, "Jarvis"), (2, "Sonu"), (103, "Stark")]

print(sorted(b))
print(sorted(c))
print(sorted(d))
print(sorted(e))
print(sorted(f))
print(sorted(g))