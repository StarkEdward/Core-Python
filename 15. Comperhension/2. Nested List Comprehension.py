# nested list Comprehension
# syntax:
# list_name = [[Expression_1 * Expression2 for item2 in range(iterable_object)] for item1 in range(iterable_object)]
# ex: lst = [[i*j for j in range(4,7)] for i in range(6,8)]
#                 inner loop                outer loop
############################################
# 1
a = [[24, 30, 36], [28, 35, 42]]
for i in range(6,8):
    for j in range(4, 7):
        pass
#  with using list Comprehension
lst = [[i*j for j in range(4,7)] for i in range(6,8)]
print(lst)
##########################################################
#






