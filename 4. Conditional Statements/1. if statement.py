# if statement

if 5 > 2:
    print("Greater")
######### or
if 5 < 2:           # its false if statement.
    print("Greater")    # This statement not execute
#########
if 5 > 2: print("Greater")
###############
if 5 > 2:
    print("Greater")
print("rest of the code")
################
if 5 > 2:
    print("greater")
    print("5 is greater than 2")
print("Rest of the code.")
##########################
# Input from user.
a = int(input("Enter Number Greater than 50: "))
if a > 50:
    print("Your have enterd: ", a)
    print(f"{a} is greater than 50")

############################
# Example 2
a = 10
if a % 2 == 0:
    print("Even Number")
##############################
# input from user.
a = int(input("Enter the value: "))
if a % 2 == 0:
    print(f"{a} is even number.")
print("This line is outside if indentation.")

