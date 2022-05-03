# Passing and returning list
# 1
def show(l):
    print(l)
    print(type(l))
    for i in l:
        print(i)
    return l

lst = [10, 20, 30, "Edward"]
new_list = show(lst)
print(new_list)
print(type(new_list))
####################################
# 2