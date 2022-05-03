from numpy import *
a = array([10, 20, 30, 40, 50])
b = a.view()
a[1] = 80
b[2] = 300
print(a, "id=", id(a))
print(b, "id=", id(b))
