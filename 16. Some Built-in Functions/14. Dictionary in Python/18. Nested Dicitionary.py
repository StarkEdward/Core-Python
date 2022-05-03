# 1 Empty nested dict
a = {1 : {}, 2 : {}, 3 : {}}
print(a)
#######################
# 2 Accessing Dictionary
a = {'course': 'Python', 'fees': 50000, 1: {'course':'java','fees':100000}}
print(a)
print(a['course'])
print(a['fees'])
print(a[1]['course'])
print(a[1]['fees'])
##########################################
# 3 Modifying dictionary
a = {'course': 'Python', 'fees': 50000, 1: {'course':'java','fees':100000}}

a['course'] = 'Machine Learning'
a[1]['fees'] = 200000

print(a)
##################################
# 4 deleting element
a = {'course': 'Python', 'fees': 50000, 1: {'course':'java','fees':100000}}
del a[1]['course']
print(a)
#################
# 5 Adding new item
a = {'course': 'Python', 'fees': 50000, 1: {'course':'java','fees':100000}}

a['duration'] = '6 months'
a[1]['teacher'] = 'Pathan Sir'
print(a)
###################
# 6 adding dictionary
a = {'course': 'Python', 'fees': 50000, 1: {'course':'java','fees':100000}}
a[2] = {'course': 'ReactJS', 'fees': 30000}
print(a)
##################################
# 7 Adding dictionary inside inner dictionary
a = {'course': 'Python', 'fees': 50000, 1: {'course':'java','fees':100000}}
a[1][2] = {'course': 'ReactJS', 'fees': 30000}
print(a)

