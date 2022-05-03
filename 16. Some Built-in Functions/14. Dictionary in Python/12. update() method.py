# this method is used to update the dictionary with the specified key value pair.
# syntax: dict_name.update(iterable)

#1
stu = {101:"Edward", 102:"Stark", 103:"Jarvis"}
print("Original Dict:")
print(stu)
print()

stu.update({104:'Python'})
print("updated dict:")
print(stu)


# 2
stu = {101:"Edward", 102:"Stark", 103:"Jarvis"}
print("Original Dict:")
print(stu)

print()

val = {'name': 'Sonu', 'Address' : 'Shahada', 105 : 'Loki'}
stu.update(val)
print(stu)





