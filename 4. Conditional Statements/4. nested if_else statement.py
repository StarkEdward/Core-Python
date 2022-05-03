# nested if else statemetn.

# example 1.
a = 5
b = 20
c = 6
d = 3
if (a > b):
    print("a is greater than b")
    if (c > d):
        print(" c is greater than d")
    else:
        print("d is greater than c")
else:
    print("b is greater than a")
    if (a > c):
        print("a is greater than c")
    else:
        print("c is greater than a")
print("Rest of the code.")

######################################################

# 2.
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

if (a > b):
    print(f"a: {a} is greater than b: {b} ")
    if (a > c):
        print(f"and also a:{a} is greater than c: {c}")
    else:
        print(f"and c: {c} is greater than a: {a}")
else:
    print(f"b: {b} is greater than a: {a}")
    if (b > c):
        print(f"and b: {b} is greater than c: {c}")
    else:
        print(f"c: {c} is greater than b: {b}")
print("Outside the nested if-else statement.")

#####################################################################################

# 2. program to check number is positive negative or zero using nested if else statement.

num = int(input("Enter a number: "))
if (num >=0):
    if (num == 0):
        print("Zero")
    else:
        print("number is Positive.")
else:
    print("Number is Negative.")