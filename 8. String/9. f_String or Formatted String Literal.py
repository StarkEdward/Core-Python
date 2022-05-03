# integer
a = 10
b = 20
print(f"{a}")
print(f"{a}{b}")
print(f"{a} {b}")
print(f"{b} {a}")
###
a = 10
b = 20
value = f"{a}"
print(value)
########################
# float
c = 10.56
d = 20.42
print(f"{c}")
print(f"{c} {d}")
print(f"{d} {c}")
#
value = f"{c}"
print(value)
#
##################
# String
f_name = "Edward"
l_name = "Stark"
print(f"{f_name}")
print(f"{f_name} {l_name}")
print(f"{l_name} {f_name}")
#
t_name = f"{f_name} {l_name}"
print(t_name)
####################
# String, Integer & Float mix
name = "Stark"
age = 26.5
no = 10
print(f"Hello My name is {name}")
print(f"My age is {age}")
print(f"{age} {name} {no}")
##########################
print()
#################################################
# integer with padding
num = 15
print(f"{num:5d}")
print(f"{num:05d}")
print(f"{num:+5d}")
print(f"{num:<5d}")
print(f"{num:*<5d}")
print(f"{num:*>5d}")
print(f"{num:^5d}")
print(f"{num:*^5d}")
print()
#################################################
# floating with padding and precision
num = 15.65
print(f"{num:8f}")
print(f"{num:8.3f}")
print(f"{num:08.2f}")
print(f"{num:+8.2f}")
print(f"{num:<8.2f}")
print(f"{num:*<8.2f}")
print(f"{num:*>8.2f}")
print(f"{num:^8.2f}")
print(f"{num:*^8.2f}")
print()
###########################################################
# String padding (s is optional
name = "Star"
print(f"{name:8s}")
print(f"{name:<8}")
print(f"{name:*<8s}")
print(f"{name:>8}")
print(f"{name:*>8}")
print(f"{name:^8s}")
print(f"{name:*^8s}")
print()
##########################################
# String Truncate
name = "StarkEdward"
print(f"{name:.3s}")
print(f"{name:5.3}")
print(f"{name:*<.3}")
print(f"{name:>5.3}")
print(f"{name:*>5.3s}")
print(f"{name:^5.3s}")
print(f"{name:*^5.3}")
print()
###################
# Some Extra stuff
price = 1234567890
print(f"{price:,}")
print(f"{price:_}")
#####
name = "Jarvis"
age = 21
print(f"My name is {name} and age is {age}")
#####
print(f"{10*8}")
#
a = 444
b = 550
print(f"{a/b:.2%}")
####
# arguement of item access
value = (10, 20)
print(f"{value[0]}")
print(f"{value[0]} {value[1]}")
####
# dict
data = {'Sonu': 2000, 'Sagar': 3000}
print(f"{data['Sonu']:d}")
print(f"{data['Sonu']:d} {data['Sagar']:d}")
###
# callin function
name = "starkedward"
print(f"{name.upper()}")
####
print(f"{{10}}")
##
# Date and Time
from datetime import datetime
today = datetime(2022, 3, 12 )
print(f"{today}")
print(f"{today:%d/%b/%Y}")
