# Aliasing list (nickname): Aliasing means giving another name to the exisiting object. It doesn't mean copying.
# Modification in a will affect b and vice versa
a = [10, 20, 30, 40, 50]
b = a
print("A:", a, id(a))
print("B:", b, id(b))

print()
print("Modifying A")
a[1] = 55
print("A:", a)
print("B:", b)

print()
print("Modifying B")
b[2] = 66
print("A:", a)
print("B:", b)
