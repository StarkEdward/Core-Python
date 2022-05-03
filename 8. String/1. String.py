# Creating String

# Single Quote
str1 = 'StarkEdard'
print(str1)

# Double Quote
str2 = "King in the North"
print(str2)

# Triple Single Quotes
str3 = '''Hello Friends
This is Stark
Good Night.'''
print(str3)

# Triple Double Quotes
str4 = """Hello Friends!
Winter is Coming!
North Remembers."""
print(str4)

# Double Quote inside Single Quotes
str5 = 'Hello "Stark Jarvis" How are you?'
print(str5)

# Single Quote insde Double Quotes
str6 = "Hello 'Stark Edward' Where are you?"
print(str6)

# Using Escape Characters
str7 = "Hello \nHow are you?"
print(str7)

# Raw String
str8 = r"Hello \nHow are you?"
print(str8)

#########################################################################
# Memory Allocation
str1 = "StarkEdward"
str2 = "StarkEdward"
str3 = "Python"
str4 = str3
print("str1:", id(str1))
print("str2:", id(str2))
print("str3:", id(str3))
print("str4:", id(str4))

# 2
str = "Jarvis"
print("str = ", id(str))
str = "Python Hatch"
print("Str = ", id(str))
################################################
# String indexing
str1 = "StarkEdward"

print(str1)
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[-1])
print(str1[-6])
print(str1[-11])

