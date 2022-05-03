# Recursion
# 1
def myfun():
    print("StarkEdward")
    myfun()         # calling itself 1000 times
myfun()
###########################
# 2
i = 0
def myfun():
    global i
    i=i+1
    print("My function:", i)
    myfun()
myfun()
#####################
# 3
import  sys
sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())      # To check limit
