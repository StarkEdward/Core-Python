# output statement
print("Welcome to North")
print()
print('Welcome to North')
print("Hello", "to", "Jarvis")
print(10)
print(15.6)

print("Hello")
print("World")
###################################
# print(object)

data = [10, 20, 21.3, 'North']  # list
print(data)

data = ("Input", 5, 4.2, 5+6j)  # Tuple
print(data)

data = {1:'Ferrari', 2:'Lamborghini', 3:'Porsche'}  # Dictionary
print(data)

########################
# print("String" sep='')
print("Like", "Share", "Subscribe")
print("Like", "Share", "Subscribe",sep = '')
print("Like", "Share", "Subscribe",sep = ' ')
print("Like", "Share", "Subscribe",sep = '***')
print("Like", "Share", "Subscribe",sep = '____')
#####################################################
# print("string", end='')
print("Hello", end='\n')
print("Hello", end =' ')
print("Edward", end = ' ')
print("Good Morning")

print("welcome", end = '\t\t')
print("Home")
####################################
# print(variable list)
a = 10
print(a)

x = 20
y = 30
print(x, y)
print(x, y, sep = ', ')
print(x, y, sep = ':')
###########################
# print("string", variable list)
m = 40
print("Value:", m)

name = "Edward"
age = 26
print("My name is", name, "and My age is", age)
# print("string", variable list, sep = None, end = "."
print("My name is", name, "and My age is", age, sep = None, end = ".")