# reduce() function:- Thsi function is used to reduce a sequence of elements to a single value by processing the elements according to a
# function supplied. It returns a single valuse.
# this function is a part of functools module so you have to import it before using.
# syntax:-
# from functools import reduce
# reduce(function_name, sequence)
###############################################
# 1
from functools import reduce
a = [10, 20, 30, 40, 50]

result = reduce(lambda n,m: n+m, a)
print(result)
print(type(result))
