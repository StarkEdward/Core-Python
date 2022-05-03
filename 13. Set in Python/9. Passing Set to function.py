# Passing set to function

def show(s):
    print(s)
    print(type(s))
    for i in s:
        print(i)

st = {10, 20, 30, "Edward"}
show(st)