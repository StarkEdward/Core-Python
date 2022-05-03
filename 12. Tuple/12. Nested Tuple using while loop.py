# 1
# a = (10, 20, 30, (50, 60))
# n = len(a)
# i = 0
# while i < n:
#     # Checking a[i] is a tuple or not
#     if type(a[i]) is tuple:
#         if len(a[i]) > 1:
#             m = len(a[i])
#             j = 0
#             while j < m:
#                 print(i, j, a[i][j])
#                 j += 1
#             i += 1
#     else:
#         print(i, a[i])
#         i += 1
###########################################################
# 2
a = ((10, 20, 30), (40, 50, 60))
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(i, j, a[i][j])
        j += 1
    print()
    i += 1
############################################################







