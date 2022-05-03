# Nested lambda function
# 1
add = lambda x = 10 : (lambda y: x + y)

a = add()
print(a(5))
##########


