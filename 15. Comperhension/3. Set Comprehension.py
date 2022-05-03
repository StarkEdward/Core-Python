# Set Comprehension represents creation of new set from an iterable object that satisfy a given condition
'''
syntax:
new_set= {expression for item in iterable_object if_statement}
There can be ero orr more if statements.
There can be one or multiple for loops.
Ex:-
set1 = {i+1 for i in range(20)}
set2 = {i for i in range(20) if i%2==0}
set3 = {i for i in ragne(20) if i%2==0 if i%3==0}

'''
#1
# without Comprehension
# set1 = {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
# new_set1 = set()
# for i in set1:
#     new_set1.add(i+1)
#
# print(new_set1)
# print(type(new_set1))

# With Comprehension
# set1 = {0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
# new_set1 = {i+1 for i in range(20)}
# print(new_set1)
###############################
# 2
# without Comprehension
# set1 = set()
# for i in range(20):
#     set1.add(i+1)
# print(set1)
# print()
# With Comprehension
# set1 = {i+1 for i in range(20)}
# print(set1)
####################################################
# 3
# set2 = {i for i in range(20)}
# print(set2)
####################################
# 4 Generating even number in list from 0 to 20
# without using set comprehension
# set2 = set()
# for i in range(20):
#     if i%2==0:
#         set2.add(i)
# print(set2)
# using Set Comprehension
# set2 = {i for i in range(20) if i%2==0}
# print(set2)
##################################################
# 5 Generate odd number in list from 0 to 20
# without using set comprehension
# set2 = set()
# for i in range(20):
#     if i % 2 == 0:
#         set2.add(i+1)
# print(set2)
# # using set Comprehension
# set2 = {i+1 for i in range(20) if i%2==0}
# print(set2)
###############################################
# 6
# without using set comprehension
# set3 = set()
# for i in range(20):
#     if i % 2 == 0:
#         if i % 3 == 0:
#             set3.add(i)
# print(set3)

# using set Comprehension
# set3 = {i for i in range(20) if i%2==0 if i%3==0}
# print(set3)
########################################################
'''
* Set comprehension with if else statement
syntax:
new_set = {expression if_statment else expression for item in iterable_object}
ex:
new_set = {i if i%2==0 else i*1000 for i in range(10)}
'''
#Example
# 1
# without using set comprehension
# set1 = set()
# for i in range(10):
#     if (i % 2) == 0:
#         set1.add(i)
#     else:
#         set1.add(i*1000)
# print(set1)
# using set Comprehension
# set1 = {i if i%2==0 else i*1000 for i in range(10)}
# print(set1)
#########################################





