# Dictionary comprehension
# 1
# without dict comprehension
# dict1 = {}
# for n in range(10):
#     dict1[n] = n*2
# print(dict1)

# with using dict comprehension
dict2 = {n:n*2 for n in range(5)}
print(dict2)
#########################################
# 2
# without dict comprehension
# dict1 = {}
# for n in range(10):
#     if n%2==0:
#         dict1[n] = n*2
# print(dict1)

# with using dict comprehension
dict2 = {n:n*2 for n in range(10) if n%2==0}
print(dict2)
########################################
# 3
# without dict comprehension
# dict1 = {}
# for n in range(20):
#     if n % 2 == 0:
#         if n % 3 == 0:
#             dict1[n] = n*2
# print(dict1)

# with using dict comprehension
dict2 = {n:n*2 for n in range(20) if n%2==0 if n%3==0}
print(dict2)
#########################################################################################
#

# without dict comprehension
# dict1 = {}
# for n in range(10):
#     if n%2==0:
#         dict1[n] = n
#     else:
#         dict1[n] = 'Invalid'
# print(dict1)

# with using dict comprehension
dict2 = {n:(n if n%2==0 else 'Invalid') for n in range(5)}
print(dict2)

#########################
# 5
lst = [(101, "Edward"), (102, "Jarvis")]
dict1 = {k:v for k,v in lst}
print(dict1)