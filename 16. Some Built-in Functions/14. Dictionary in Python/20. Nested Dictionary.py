# 1 Accessing Nested Dictionary
# a = {1: {'course': 'Python', 'fees': 50000},
#      2: {'course': 'java', 'fees': 100000}}
#
# print(a)
# print(a[1])
# print(a[2])
# print(a[1]['course'])
# print(a[1]['fees'])
# print(a[2]['course'])
# print(a[2]['fees'])
################################
# 2 Modifying Nested Dictionary
# a = {1: {'course': 'Python', 'fees': 50000},
#      2: {'course': 'java', 'fees': 100000}}
#
# a[1]['course'] = 'Machine Learning'
# a[2]['fees'] = 200000
#
# print(a)
#############################
# 3 Deleting element from dictionary
# a = {1: {'course': 'Python', 'fees': 50000},
#      2: {'course': 'java', 'fees': 100000}}
#
# del a[1]['course']
# print(a)
#############################
# 4 Adding new item to Dictionary
# a = {1: {'course': 'Python', 'fees': 50000},
#      2: {'course': 'java', 'fees': 100000}}
#
# a[1]['duration'] = '6 Month'
# a[2]['teacher'] = 'Vinay sir'
#
# print(a)
#######################################
# 5 Adding dictionary
a = {1: {'course': 'Python', 'fees': 50000},
     2: {'course': 'java', 'fees': 100000}}
a[3] = {'course': 'ReactJS', 'fees': 30000}
a[1]['sub_course'] = {'course': 'AI', 'fees': 75000}
print(a)
#############################################################


