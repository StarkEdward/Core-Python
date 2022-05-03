# This function returns the length (the number of item) of an object.
# This argument may be a sequence (such as sring, bytes, tuple, list or range) or a collection ( such as dictionary, set or frozen set).
# syntax: len(arg)
############################
# 1
a = "StarkEdward"
b = [10, 20, 30]
c = (10, 20, 30, 40, 50)
d = {10, 20, 30, 40}
e = {101:'Edward', 102 : "Jarvis", 103: "Stark"}
f = [[10,20], [30,40], [50,60]]
g = [(101, "Edward"), (102, "Jarvis"), (103, "Stark")]

print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))
print(len(g))



