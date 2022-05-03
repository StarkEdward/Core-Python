# Global Keyword
# 1
# a = 50
# def show():
#     global a
#     print('Inside function:', a)
# show()
# print("Outside Function :", a)
##################
# 2
# i = 0
# def show():
#     global i
#     # i = i + 1
#     print("I:", i)
# show()
# print(i)
#################
# 3
i = 0
def myfun():
    global i
    while i < 5:
        i += 1
        print(i)
myfun()
print("Outside function: ", i)
