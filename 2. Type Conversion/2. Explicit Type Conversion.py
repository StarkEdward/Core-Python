# Explicit type conversion

a = 5
b = 2
value = a/b
print(value, type(value))
int_value = int(value)
print(int_value, type(int_value))

q = 20
u = "10"
print(u, type(u))
r = q + int(u)
print(r, type(r))

# Float to Integer
n = 10.36
print(n, type(n))
vn = int(n)
print(vn, type(vn))

# Integer to float
m = 15
print(m, type(m))
vm = float(m)
print(vm, type(vm))

# Integer to complex
n = 10
print(n, type(n))
vn = complex(n)
print(vn, type(vn))

# Float to Complex
n = 12.65
print(n, type(n))
vn = complex(n)
print(vn, type(vn))

# Integer to string
n = 10
print(n, type(n))
vn = str(n)
print(vn, type(vn))

# String to Integer
n = '10'
print(n, type(n))
vn = int(n)
print(vn, type(vn))

# Float to String
n = 36.5
print(n, type(n))
vn = str(n)
print(vn, type(vn))

# String to Float
n = "125.65"
print(n, type(n))
vn = float(n)
print(vn, type(vn))

# String to tuple
n = "StarkEdward"
print(n, type(n))
vn = tuple(n)
print(vn, type(vn))

# Tuple to String
n = ("Sagar", "Sonu", "Vikky")
print(n, type(n))
vn = str(n)
print(vn, type(vn))

# string to list
n = "StarkEdward"
print(n, type(n))
vn = list(n)
print(vn, type(vn))

# Tuple to list
n = ("Sagar", "Sonu", "Vikky")
print(n, type(n))
vn = list(n)
print(vn, type(vn))

# List to Tuple
n = ["Goa", "Dhule", "Pune"]
print(n, type(n))
vn = tuple(n)
print(vn, type(vn))

# integer to binary
n = 10
print(bin(n))

# Binary to integer
n = 0b1111
print(int(n))

# Integer to Octal
n = 10
print(oct(n))

# Octal to Integer, float, Binary, Hex
n = 0o12
print(int(n))
print(float(n))
print(bin(n))
print(hex(n))
print(str(n))

# Integer to Hex
n = 10
print(hex(n))

# Hex to Integer, String, Float, Binary, Octal
n = 0xa
print(int(n))
print(str(n))
print(float(n))
print(bin(n))
print(oct(n))




