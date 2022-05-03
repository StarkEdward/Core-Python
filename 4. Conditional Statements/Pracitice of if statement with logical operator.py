# if statement with logical operator.

# and statement
# 1. both are true.
if 5 > 2 and 7 >3:
    print("if statement with Logical operator")     # gives output
print("Rest of the code.")  # complsary gives output

# 2. any one is true
if 5 > 2 and 7 < 3:
    print("if statment with logical operator")  # not gives output
print("rest of the code.") # cumplsary gives output

#####################################################################################

# or statement
# 1. both are true
a = 5
b = 3
c = 7
if (a > b) or (c > b):
    print("This if statement Execute.")                     # gives output
    print("a is greater than b and c is greater than b")    # gives output
print("rest of code")   # cumplsary gives output
# 2. any one is true.
a = 5
b = 3
c = 7
if (a > b) or (c < b):
    print("This if statement Execute.")                     # gives output
    print("a is greater than b and c is greater than b")    # gives output
print("rest of code")   # cumplsary gives output

# 3. None are ture.
a = 5
b = 3
c = 7
if (a < b) or (c < b):
    print("This if statement Execute.")                     # not gives output
    print("a is greater than b and c is greater than b")    # not gives output
print("rest of code")   # cumplsary gives output

############################################################################################

# not statement
# 1
a = 10
b = 6
if not(a > b):
    print("grater ")    # not execute
print("rest ")   # cumplsary gives output
# 2
a = 10
b = 6
if not(a < b):
    print("grater ")    # gives output
print("rest ")   # cumplsary gives output

###############################################################################