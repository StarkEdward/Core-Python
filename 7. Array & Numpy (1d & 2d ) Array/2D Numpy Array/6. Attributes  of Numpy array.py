from numpy import *
a = array([101, 102, 103, 104, 105, 106])
b = array([[10, 20, 30, 40], [50, 60, 70, 80]])
print()
# ndim Attributes
print("1D Array ndim:", a.ndim)
print("2D Array ndim:", b.ndim)
print()
# Shape Attributes
# for 1D Array shape elements in the row
# for 2D Array shape specifies number of row and column in each row
print("1D Array Shape:", a.shape)
print("2D Array Shape:", b.shape)
print()
# Size Attributes
print("1D Array Size:", a.size)
print("2D Array Size:", b.size)
print()
# itemsize Attributes
print("1D Array itemsize:", a.itemsize)
print("2D Array itemsize:", b.itemsize)
print()
# dtype Attributes
print("1D Array dtype:", a.dtype)
print("2D Array dtype:", b.dtype)
print()
# nbytes Attributes
print("1D Array nbytes:", a.nbytes)
print("2D Array nbytes:", b.nbytes)
################################################
