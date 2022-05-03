# if_elif_else

# greater than less than or equal.
a = int(input("a: "))
b = int(input("b: "))

if (a > b):
    print("a is greater than b")
elif (a == b):
    print("a and b are equal")
else:
    print("a is less than b")
######################################################
# 2. What day is today.
day = input("Enter day: ").title()
if (day == "Monday"):
    print("Today is Monday")
elif (day == "Tuesday"):
    print("Today is Tuesday")
elif (day == "Wednesday"):
    print("Today is Wednesday")
elif (day == "Thursday"):
    print("Today is Thursday")
elif (day == "Friday"):
    print("Today is Friday")
elif (day == "Saturday") or (day == "Sunday"):
    print("Today is Holiday")
else:
    print("Please Enter correct day.")

######################################################

# 3. positive negative or zero

num = int(input("Enter a Number: "))

if (num == 0):
    print("Number is zero")
elif (num > 0):
    print("Numb is Positive")
else:
    print("number is Negative")

#############################################################

