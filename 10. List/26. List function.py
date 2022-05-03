# list() Function
# This is used to create a list. It returns a mutable lsit of elements.
# syntax:-  list()      <---- Creates Empty list
# list(iterable _Object)  <----- Creates a list of elements
# Ex:- list()
# list("Edward")

# We can use list and range function to create a list.
# Syntax:- list(range(start, stop, stepsize)
# Ex:- list(range(0,5)

# 1 Creating Empty list using list function
a = list()
print(a)
print(type(a))
############################
# 2 Creating Element list using list function
a = list("Edward")
print(a)
print(type(a))
###############################
# 3
a = list(range(0, 5))
print(a)
print(type(a))
####################
# 4 create list of range by user input
n = int(input("Enter range for list: "))
a = list(range(n))
print(a)

