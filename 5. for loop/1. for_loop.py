# getting every char on new line from string
st = "Stark Edward"
for s in st:
    print(s)
print("Rest of the code")

# getting  everry char in Reverse on new line from a string
st = " Stark Jarvis"
for s in st[::-1]:
    print(s)

# gettomg everu char seprated by dual space from string.
st = "StarkEdward"
for s in st:
    print(s, end="  ")
print("\nOutside for loop")

# Reverse a string.
st = "Chandrakiran"
for c in st[::-1]:
    print(c, end="")
print("\nOutside for loop")

# Reverse a string sep by extra space.
st = "CHANDRAKIRAN"
for c in st[::-1]:
    print(c, end="  ")
print("\nRest Of the Code")

# list example
li = ["Stark", 3, "Jarvis", 25, "Buddha"]
for l in li:
    print(l)
print("Rest of the Code.")

# Reverse a list
li = ["Stark", 3.0, "Jarvis", 25, "Buddha"]
for l in li[::-1]:
    print(l)
print("Rest of the Code.")

# reverse a list in single line
li = ["Stark", 3, "Jarvis", 25, "Buddha"]
for l in li[::-1]:
    print(l, end=" ")
print("\nRest of the Code.")
