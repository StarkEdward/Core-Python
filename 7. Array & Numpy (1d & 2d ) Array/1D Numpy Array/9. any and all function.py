# any() Function
from numpy import *
a = array([100, 200, 300, 400, 500])
b = array([100, 20, 30, 400, 50])
c = a == b
print(any(c))
d = a < b
print(d)
print(any(d))

#################################
# all() Function
from numpy import *
a = array([100, 200, 300, 400, 500])
b = array([100, 200, 300, 400, 500])
c = a == b
print(all(c))