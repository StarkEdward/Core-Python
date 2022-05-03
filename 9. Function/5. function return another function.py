# function return antehr funtion
def disp():
    def show():
        return("Show function")
    print("Disp Function")
    return show
r_sh = disp()
print(r_sh())
###############################################
# 2
def disp(sh):
    print("Disp Function")
    return sh
def show():
    return "Show function"

r = disp(show)
print(r())