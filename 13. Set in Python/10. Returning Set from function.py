
def show(s):
    print(s)
    print(type(s))
    for i in s:
        print(i)
    return s

st = {10, 20, 30, "Edward"}
new_st = show(st)
print(new_st)
print(type(new_st))