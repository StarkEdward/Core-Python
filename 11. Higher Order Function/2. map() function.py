# map() function: This function executes a specified function on each elements of the itterable(sequence) and perhaps changes the elements.
# Syntax:- map(function_name, iterable)
# Function_name:- It's a name of a function which perform an operationon all the elements of the sequence and modifed elements are resturned which can be stored in another sequence.
# iterable:- Iterable may be either a sequence, list, string , tuple, a container which supports iteration , or an iterator.
#################################
# a = [10, 20, 30, 40, 50]

# def inc(n):
#     return n+2
# result = map(inc, a)
# for i in result:
#     print(i)
# # print(result)
# # print(type(result))
# ############
# 2
a = [10, 20, 30, 40, 50]

def inc(n):
    return n+2
result = list(map(inc, a))
print(result)
for i in result:
    print(i)
####################
# 3
# a = [10, 20, 30, 40, 50]
#
# result = list(map(lambda n : (n+2), a))
#
# print(result)
# for i in result:
#     print(i)
#######################################################
a = [10, 20, 30, 40, 50]
b= [1, 2, 3, 4, 5]
result = list(map(lambda n, m: n+m, a,b))
print(result)
for i in result:
    print(i)
#########################################################



