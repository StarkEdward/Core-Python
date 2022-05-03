# # create array example 1
# import array
# roll = array.array('i', [101, 102, 103, 104, 105])
# print(roll[0])
# print(roll[1])
# print(roll[2])
# print(roll[3])
# print(roll[4])
#
# # create array example 2
# import array as ar
# roll= ar.array('i', [101, 102, 103, 104, 105])
# print(roll[2])
# print(roll[3])
#
# # create array example 3
# from array import *
# roll = array('i', [101, 102, 103, 104, 105])
# print(roll[0])
# print(roll[4])
#
# # create array example 4 (float)
# from array import *
# per = array('f', [10.5, 65.6, 13.25, 0.6])
# print(per[0])
# print(per[1])
# print(per[2])
# print(per[3])
#
# # create array example 5 (int to float)
# from array import *
# roll = array('f', [10, 2.5, 30, 40, 50.6])
# print(roll[0])
# print(roll[1])
# print(roll[2])
# print(roll[3])
# print(roll[4])

# Accessing Array using while loop
# from array import *
#
# stu_roll = array('i', [101, 102, 103, 104, 105, 106])
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1
#
# from array import *
#
# stu_roll = array('i', [101, 102, 103, 104, 105, 106])
# n = len(stu_roll)
# i = 0
# while i < n:
#     print("Index", i, "=", stu_roll[i])
#     i += 1

# Accessing Array using for loop
# from array import *
# roll = array('i', [101, 102, 103, 104, 105])
# # without using index:
# for element in roll:
#     print(element)
# #+++++++++++++++++++
# # with using index:
# # n = len(roll)
# for i in range(len(roll)):
#     print(roll[i])



# append() method in array

# from array import *
# roll = array('i', [101, 102, 103, 104, 105])
# roll.append(106)
# roll.append(107)
# # roll.append(int(input("Enter New Number:")))        # getting input from user in array
#
# n = len(roll)
# i = 0
# while (i < n):
#     print(roll[i])
#     i += 1

# Getting user input in array
# getting input from user using for loop
# from array import *
# stu_roll = array('i', [])
# n = int(input("How many element? "))
# for i in range(n):
#     stu_roll.append(int(input("Enter Element: ")))
#
# for i in range(len(stu_roll)):
#     print(stu_roll[i])

# Getting input from user using while loop
# from array import *
# stu_roll = array('i', [])
# n = int(input("Enter number of element: "))
# i = 0
# j = 0
# while i < n:
#     stu_roll.append(int(input("Enter element: ")))
#     i += 1
# while j < len(stu_roll):
#     print(stu_roll[j])
#     j += 1


# insert() method in array

# from array import *
# stu_roll = array('i', [101, 102, 103, 104, 105])
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i], end = " ")
#     i += 1
#
# print("\nAfter Insert ")
# stu_roll.insert(1, 111)
# stu_roll.insert(3, 222)
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i], end = " ")
#     i += 1

# pop() method in array
# from array import *
# roll = array('i', [101,102,103,104,105])
# roll.pop()
# i = 0
# while i < len(roll):
#     print(roll[i])
#     i += 1
# pop(positionNumber)
# from array import *
# roll = array('i', [101,102,103,104,105])
# # roll.pop(2)
# r = roll.pop(2)
# i =0
# while i < len(roll):
#     print(roll[i])
#     i += 1
# print("Removed Element: ", r)

# remove()
# from array import *
# roll = array('i', [101,102,103,101,104,105])
# i = 0
# while i < len(roll):
#     print(roll[i], end = " ")
#     i += 1
# print("After using remove()")
# roll.remove(101)
# i = 0
# while i < len(roll):
#     print(roll[i], end = " ")
#     i += 1


# # index()
#
# from array import *
# roll = array('i', [101,102,101,104,105])
# print(roll.index(101))
# print(roll.index(104))

# reverse()
# from array import *
# roll = array('i', [101,102,103,104,105])
# roll.reverse()
# i = 0
# while i < len(roll):
#     print(roll[i], end = " ")
#     i += 1

# extend()
# from array import *
# roll = array("i", [101, 102, 103, 104, 105])
# arr = array('i', [106,107])
# roll.extend(arr)
# i = 0
# while i < len(roll):
#     print(roll[i], end = " ")
#     i += 1

# Slicing on Array

# from array import *
# roll = array('i', [101, 102, 103, 104, 105, 106, 107, 108])
# print("Original Array")
# for i in range(len(roll)):
#     print(i, '=', roll[i])
# print("******************")
# a = roll[2:5]   # print from index no 2 to upto index no 4
# for i in a:
#     print(i)
# print("******************")
# a = roll[:]     # display array
# for i in a:
#     print(i)
# print("******************")
# a = roll[4:]    # display from index no 4 upto last array
# for i in a:
#     print(i)
# print("******************")
# a = roll[-3:]   # display last 3 elements
# for i in a:
#     print(i)
# print("******************")
# a = roll[:-3]   #display from -4 to first array
# for i in a:
#     print(i)
# print("******************")
# a = roll[-5:-3] # -5(-3) = -5 +3 = -{2} means only 2 elements display
# for i in a:
#     print(i)
# print("******************")
# a = roll[0:8:2]     # with step of 2
# for i in a:
#     print(i)

# use slicing in for loop
from array import *
roll = array('i', [101,102,103,104,105,106,107])
for i in roll[1:5]:
    print(i)