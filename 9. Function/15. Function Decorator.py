def decor(num):
    def inner():
        print("IF: Before Enhancing function")
        num()
        print("IF: After Enhancing Function")
    return inner
@decor
def num():
    print("We wil you tis function")
    print("and will enhance this in decorator.")

num()
################################################################
# 2
def decor(num):
    def inner():
        a = num()
        add = a + 5
        return add
    return inner

@decor
def num():
    return 10
print(num())
#########################################################
# 3
def decor1(num):
    def inner():
        b = num()
        multi = b * 5
        return multi
    return inner

def decor(num):
    def inner():
        a = num()
        add = a + 5
        return add
    return inner

@decor1
@decor

def num():
    return 10
# num = decor(decor1(num))
print(num())






