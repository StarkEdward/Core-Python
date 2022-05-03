# if else statement

# 1. program on number is  greater or less

a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

if (a > b):
    print("Greater")
    print(f"{a} is greater than {b}.")
else:
    print("Smaller")
    print(f"{a} is smaller than {b}.")
print("Rest of the Code")

# shorthand if else: in one line
print(f"{a} is greater than {b}.") if (a > b) else print(f"{a} is smaller than {b}.")

###############################################################

# 2. even or odd program.

num = int(input("Enter any number to check: "))
if num % 2 == 0:
    print(f"{num} is Even Number.")
else:
    print(f"{num} is Odd number.")

###############################################################

# 3. leap year using if else

year = int(input("Enter year to check: "))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print(f"{year} is Leap year.")
else:
    print(f"{year} is Common year.")
print("\nThank you for visiting.")

##################################################################

# 4. Number is positive or negative

num = int(input("Enter Number: "))
if (num > 0):
    print(num, "is Positive Number.")
else:
    print(num, "is Negative Number.")