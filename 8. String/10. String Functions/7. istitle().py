str1 = 'Hello World'
str2 = 'HELLO'
print(f"{str1.istitle()}\n{str2.istitle()}")

# 2

str1 = "Stark Edward".istitle()
str2 = 'star edward'.istitle()
print(f"{str1}\n{str2}")

# 3 user input:
str = input("Enter a string: ").istitle()
print(str)
