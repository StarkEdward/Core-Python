# get() method: This method returns the value of the specified key.
# if key is not found then it will return none or default value.
# syntax:- dict_name.get(key, defaultvalue)
#####################################
# 1
stu = {101: "Jarvis", 102:"Edward", 103 : "Stark"}
print("Original Dict: ")
print(stu)
print()

d = stu.get(101, "Nahi hai")
print(d)
##############################
# 2
stu = {101: "Jarvis", 102:"Edward", 103 : "Stark"}
print("Original Dict: ")
print(stu)
print()

print(stu.get(104, "Nahi_Hai"))
##################################################



