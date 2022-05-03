# input statement

name = input()
print(name)

name = input("Enter Your First Name: ")
print(name)

name = input('Enter Your Last Name: ')
print(name)

mobile = input("Enter Your Mobile Number: ")
print(mobile, type(mobile))

name = input("What is your Name? ")
print("Your Name is", name)

# use of type Conversion in input statement.
mobile = input("Enter Your Mobile Number: ")
mb = int(mobile)
print(mobile, type(mobile))
print(mb, type(mb))

# or

mobile = int(input("Enter Your Mobile Number: "))
print(mobile, type(mobile))

price = float(input("Total Price: "))
print(price, type(price))

equation = complex(input("Enter Complex Number: "))
print(equation, type(equation))

list = list(input("Enter all the Students Name: "))
print(list, type(list))

tup = tuple(input("Enter something: "))
print(tup, type(tup))


