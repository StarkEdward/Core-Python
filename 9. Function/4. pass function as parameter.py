# pass a Function as Parameter
def disp(sh):
    print("Disp Function" + sh())

def show():
    return " Show Function"

disp(show)
#################
# 2
def disp(sh):
    return "Display Functin" + sh()

def show():
    return " Show Function"

print(disp(show))