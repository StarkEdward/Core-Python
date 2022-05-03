# Clear() method is used remove all elements to the set.
# syntax: set_name.clear()
#
a = {10, 20, "Edward"}
print("Before Clear", a, id(a))
a.clear()
print("After Clear:", a, id(a))