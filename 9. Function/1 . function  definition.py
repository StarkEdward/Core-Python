# write once and use it as many time you need.

# defining a function
def disp():
    name = "Stark Edward"
    print("welcome to", name)

# calling a function
disp()
disp()
disp()
#####################################################################
# Divide large task into many small task, helpful for debuging code

# Defining Function
# Separate function for addition
def add():
    x = 10
    y = 20
    c = x + y
    print(c)
add()
# Separate function for subtraction
def sub():
    x = 10
    y = 20
    c = y - x
    print(c)
sub()
##############################################################
# Function without Argument and parameter
# Defining a Function without Parameter
def add():
    x = 10
    y = 20
    c = x + y
    print(c)
# Calling a Function without Argument
add()
###################################
# Defining a function with Parameter and Argument
def add(y):
    x = 10.2365
    c = x + y
    print(c)
# Calling a function with argument
add(20.63)
################

def add(y):
    x = 10.2365
    print(x + y)
    print(f"Formatted output {x+y:5.2f}")

# Calling a function with argument
add(20)
###################################################################################

