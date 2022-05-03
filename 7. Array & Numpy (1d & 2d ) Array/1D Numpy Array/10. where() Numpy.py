# where()
from numpy import *
a = array([150, 200, 300, 40, 500])
b =array([100, 201, 30, 400, 50])
result = where(a>b, a, b)
print(result)

result = where(a<b, a, b)
print(result)