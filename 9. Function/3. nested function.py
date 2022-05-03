# Nested Function

def disp():
    def show():
        print("Show function")
    print("Display Function")
    show()
disp()
###################################
def disp():
    def show():
        return 'Show Function'
    res = show() + "Disp Function"
    return res
a = disp()
print(a)
#

def disp(st):
    def show():
        return 'Show Function '
    res = show() + st + " Disp Function"
    return res
a = disp("Edward")
print(a)
################
def cal():
    def add(y):
        x = 10
        c = x + y
        return c
    def sub(y):
        x = 10
        c = y - x
        return c
    return print(add(20)), print(sub(20))
cal()
