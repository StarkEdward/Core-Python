#
# 1
# def val(x):
#     x = 15
#     print(x, id(x))
#
# x = 10
# val(x)
# print(x, id(x))
#########################
# 2
# def val(x):
#     print(x, id(x))
#     x = 15
#     print(x, id(x))
#
# x = 10
# val(x)
# print(x, id(x))
#################################
# 3
# def val(lst):
#     print("IFBA:", lst, id(lst))
#     lst.append(4)
#     print("IFAA:", lst, id(lst))
#
# lst = [1, 2, 3]
# print("BCF:", lst, id(lst))
# val(lst)
# print("ACF:", lst, id(lst))
########################################
# 4
# def val(a):
#     a = 15
#     print(a, id(a))
# x = 10
# val(x)
# print(x, id(x))
################################
# 5
# def val(l):
#     l.append(4)
#     print("IFAA:", l, id(l))
#
# lst = [1, 2, 3]
# print("BCF:", lst, id(lst))
# val(lst)
# print("ACF:", lst, id(lst))
#############################################
# 6
def val(lst):
    print("IFBA:", lst, id(lst))
    lst = [11, 22, 33]
    print("ACNL:", lst, id(lst))
lst = [1, 2, 3]
print("BCF:", lst, id(lst))
val(lst)
print("ACF:", lst, id(lst))






































