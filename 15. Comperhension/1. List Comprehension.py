# Comprehension contains very compact coe usually a single statement that perform a task.
# 1 List Comprehension
# 2 Set Comprehension
# 3 Dictionary Comprehension
###################################
# 1 List Comprehension
'''
List comprehension represent creation of new list from an iterable object that satisfy a given condition.
# syntax:
new_list = [expression for item in iterable_object if_statement]
There can be zero or more If statements
There can be one or multiple for loop
ex:
ls1 = [i+1 for i in range(20)]
ls2 = [i for i in range(20) if i%2==0]
ls3 = [i for i in range(11) if i%2==0 if i%3==0]

'''
# 1
# without list comprehension
# lst1 = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# new_lst1 = []
# for i in lst1:
#     new_lst1.append(i+1)
# print(new_lst1)
#
# # Using list Comprehension
# lst2= [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# new_lst2 = [i+1 for i in lst2]
# print(new_lst2)
###################
# 2
# new_lst1 = []
# for i in range(20):
#     new_lst1.append(i+1)
# print(new_lst1)
#
# # Using list Comprehension
# new_lst2 = [i+1 for i in range(20)]
# print(new_lst2)
######################################
# 3
# ls1 = [i+1 for i in range(20)]
# print(ls1)
########################
# 4 Generating even number in list from 0 to 20
# without using list comprehension
# ls2 =  []
# for i in range(20):
#     if i % 2 == 0:
#         ls2.append(i)
# print(ls2)
# # using list Comprehension
# ls2 = [i for i in range(20) if i%2==0]
# print(ls2)
##########################
# 5 Generate odd number in list from 0 to 20
# without using list comprehension
# ls2 =  []
# for i in range(20):
#     if i % 2 == 0:
#         ls2.append(i+1)
# print(ls2)
# # using list Comprehension
# ls2 = [i+1 for i in range(20) if i%2==0]
# print(ls2)
###################################################
# 6
# without using list comprehension
# ls3 =  []
# for i in range(20):
#     if i % 2 == 0:
#         if i%3==0:
#             ls3.append(i)
# print(ls3)
# print()
# # using list Comprehension
# ls2 = [i for i in range(20) if i%2==0 if i%3==0]
# print("New list:", ls2)
#######################################################################
'''
* List Comprehension with If else Statement
Syntax:
new_list = [expression if statement else expression for item in iterable_object]
ex:
new_list = [i if i%2==0 else 'Invalid' for i in range(10)]
'''
# Examples
#1
# without using list comprehension
ls =  []
for i in range(10):
    if i % 2 == 0:
        ls.append(i)
    else:
        ls.append("Invalid")
print(ls)
print()
#  with using list Comprehension
new_lst1 = [i if i%2==0 else 'invalid' for i in range(10)]
print("New list: ", new_lst1)

