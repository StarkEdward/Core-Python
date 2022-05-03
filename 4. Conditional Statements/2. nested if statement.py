# nested if statement
# 1. situation
if (5>2):
    print("Greater")
    print("5 is greater than 2")
    if(6>2):
        print("6 is greater than 2")
print("Rest of the Code. not include in if statement")
# 1.1 situation
if (5>2):
    print("Greater")
    print("5 is greater than 2")
    if(6<2):
        print("6 is greater than 2")
print("Rest of the Code. not include in if statement")
# 1.2 situation
if (5<2):
    print("Greater")
    print("5 is greater than 2")
    if(6>2):
        print("6 is greater than 2")
print("Rest of the Code. not include in if statement")

# task : program to find greater number from 3 user input number using nested if statement.
a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("enter 3rd Number: "))
if (a > b):
    print(f"{a} is Greater than {b}")
    if (a > c):
        print(f"{a} is also greater than {b} and {c}")
    if (a < c):
        print(f"but {a} is less than {c}")
if (b > a):
    print(f"{b} is greater than {a}")
    if (b > c):
        print(f"{b} is also greater than {a} and {c}")
    if (b < c):
        print(f"but {b} is less than {c}")
print("this line not include in any if statement. ")

