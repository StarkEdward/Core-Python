# Integer : It's nothing but string
print("************** Integer *****************")
print("{}".format(10))                      # Do not write space between {}
print("{} {}". format(10, 20))
print("{}      {}".format(10, 20))
print("{0}".format(10))
print("{0} {1}".format(10, 20))
print("{1} {0}".format(10, 20))
print("{num1}".format(num1=10))
print("{num1} {num2}".format(num1=10, num2=20))
print("{num2} {num1}".format(num1=10, num2=20))

####################################################################
# Float : It's nothing but string
print("**************** Float ****************")
print("{}".format(10.56))
print("{} {}".format(10.56, 20.42))
print("{0}".format(10.56))
print("{0} {1}".format(10.56, 20.42))
print("{1} {0}".format(10.56, 20.42))
print("{num1}".format(num1=10.56))
print("{num1} {num2}".format(num1=10.56, num2=20.42))
print("{num2} {num1}".format(num1=10.56, num2=20.42))

###############################################################
# String
print("**************** String ****************")
print("{}".format("Edward"))
print("{} {}".format("Stark", "Edward"))
print("{0}".format("Edward"))
print("{0} {1}".format("Stak", "Edward"))
print("{1} {0}".format("Stark", "Edwdard"))
print("{str1}".format(str1="Stark"))
print("{str1} {str2}".format(str1="Stark", str2="Edward"))
print("{str2} {str1}".format(str1="Stark", str2="Edward"))

####################################################################
# Integer and String
print("Hello My name is {}".format("Edward"))
print("{} {}".format(10, "Edward"))
print("{0} {1}".format(10, "Edward"))
print("{1} {0}".format(10, "Edward"))
print("{num1} {str1}".format(num1=10, str1="Edward"))
print("{str1} {num1}".format(num1=10, str1="Edward"))

##################################################################
# Integer : Specifying just defining "type"
print("************** Integer *****************")
print("{}".format(15))          # String
print("{:d}".format(15))
print("{:d} {:d}".format(15, 30)) # Integers
print("{0:d}".format(15))
print("{0:d} {1:d}".format(15, 30))
print("{num:d}".format(num=15))
print("{num1:d} {num2}".format(num1=15, num2=30))

#########################################################################
# Integer: using padding
print("************** Integer *****************")
print("{num:d}".format(num=15))
print("{num:5d}".format(num=15))
print("{num:05d}".format(num=15))
print("{num:+5d}".format(num=15))
print("{num:<5d}".format(num=15))
print("{num:*<5d}".format(num=15))
print("{num:*>5d}".format(num=15))
print("{num:^5d}".format(num=15))
print("{num:*^5d}".format(num=15))
#####################################
# Float : just specifying type
print("**************** Float ****************")
print("{}".format(15.65))
print("{:f}".format(15.65))
print("{:f} {:f}".format(15.65, 30.25))
print("{0:f}".format(15.65))
print("{0:f} {1:f}".format(15.65, 30.25))
print("{1:f} {0:f}".format(15.65, 30.25))
print("{num:f}".format(num=15.65))
print("{num1:f} {num2:f}".format(num1=15.65, num2=30.25))
print("{num2:f} {num1:f}".format(num1=15.65, num2=30.25))
print()
######################################################
# float : using padding and precision
print("{num:f}".format(num=15.65))
print("{num:8f}".format(num=15.65))
print("{num:8.3f}".format(num=15.65))
print("{num:+8.2f}".format(num=15.65))
print("{num:08.2f}".format(num=15.65))
print("{num:<8.2f}".format(num=15.65))
print("{num:*<8.2f}".format(num=15.65))
print("{num:>8.2f}".format(num=15.65))
print("{num:*>8.2f}".format(num=15.65))
print("{num:^8.2f}".format(num=15.65))
print("{num:*^8.2f}".format(num=15.65))
print()
#########################################################
# string : padding (s is optional for string
print("{:8s}".format("Edward"))
print("{:08s}".format("Edward"))
print("{:<8s}".format("Edward"))
print("{:*<8s}".format("Edward"))
print("{:>8s}".format("Edward"))
print("{:*>8s}".format("Edward"))
print("{:^8s}".format("Edward"))
print("{:*^8s}".format("Edward"))
print()
####################################################
# Truncating String
print("{:.3s}".format("Stark"))
print("{:8.3}".format("stark"))
print("{:<8.3}".format("Stark"))
print("{:*<8.3}".format("Stark"))
print("{:>8.3}".format("Stark"))
print("{:*>8.3}".format("Stark"))
print("{:^8.3}".format("Stark"))
print("{:*^8.3}".format("Stark"))
print()
########################################################
# Some Extra stuff:

print("{:,}".format(1234567890))  # A Thousand Separator
print("{:_}".format(1234567890))

name = "Stark"
age = "26"
print("My name is {} and age is {}".format(name, age))

a = 444
b = 550
print("{:.2%}".format(a/b))
# accessing arugment items
value = (10, 20)
print("{0[0]} {0[1]}".format(value))
# dict
data1 = {'sagar': 2000, 'sonu': 3000}
print("{0[sagar]:d} {0[sonu]:d}".format(data1))
print("{d[sagar]:d} {d[sonu]:d}".format(d=data1))
print("{sagar} {sonu}".format(**data1))     # format parameter

















