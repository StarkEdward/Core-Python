# 1 converting 1D array into 2D array
from numpy import *
a = array([1, 2, 3, 4, 5, 6])
b = reshape(a, (2, 3))
print("1D array=", a)
print("After Converting")
print("2D array =",b)
########################################
# 2 Converting 1D array into 3D array
from numpy import *
c = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
d = reshape(c, (2, 3, 2))
print("1D Array= ", c)
print("After Converting")
print("3D Array=", d)
#############################################
# 3 Converting 2D array into 1D array
from numpy import *
e = array([[1, 2, 3],
           [4, 5, 6]])
f = reshape(e, (6))
print("2D Array= ", e)
print("After Converting")
print("1D Array=", f)
##################################
# 3 Converting 3D Array into 1D array
from numpy import *
e = array([ [ [1, 2], [3, 4], [5, 6] ], [[7, 8], [9, 10], [11, 12]]])
f = reshape(e, (12))
print("3D Array= ", e)
print("After Converting")
print("1D Array=", f)
##############################################
# flatten()
# to convert 2d or 3d Array into 1D array
from numpy import *
a = array([ [1, 2, 3], [4, 5, 6]])
b = a.flatten()
print(a)
print(b)
##########################