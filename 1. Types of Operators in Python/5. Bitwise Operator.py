# Bitwise Operators

# Bitwise AND (&)
a = 10                      # 0000 1010 = 10
b = 15                      # 0000 1111 = 15
print("a & b = ", a & b)    # 0000 1010 = 10

# Bitwse OR (|)
a = 10                       # 0000 1010 = 10
b = 15                       # 0000 1111 = 15
print("a | b = ", a | b)     # 0000 1111 = 15

# Bitwise XOR (^)
a = 10                          # 0000 1010 = 10
b = 15                          # 0000 1111 = 15
print("a ^ b = ", a ^ b)        # 0000 0101 = 5

# Bitwase NOT (~)
a = 10                          # 0000 1010
print("~a = ", ~a)              # 1111 0101 = -11

# Bitwise Left Shift (<<)
a = 10                             # 0000 1010
print("a << 2 = ", a << 2)         # 0010 1000 = 40

# Bitwise Right Shift (>>)
a = 10                           # 0000 1010
print("a >> 2 = ", a>>2)         # 0000 0010 = 2