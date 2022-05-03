# linspace() Function

# from numpy import *
# a = linspace(1, 8)
# print(a)
###########################
# from numpy import *
# a = linspace(1,8,5)
# print(a)
#############################
# from numpy import *
# a = linspace(1,8,5, endpoint= False)
# print(a)
#################################

# 1
# from numpy import *
# a = linspace(1, 8, 5)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
##########################################
# 2 For loop
# without index

# from numpy import *
# a = linspace(1, 8, 5)
# for ele in a:
#     print(ele)

# with index
# from numpy import *
# a = linspace(1, 8, 5)
# for i in range(len(a)):
#     print(a[i])
############################################
# 3 While Loop
# from numpy import *
# a = linspace(1, 8, 5)
# i = 0
# while i < len(a):
#     print("Index", i, "=", a[i])
#     i += 1
#########################################