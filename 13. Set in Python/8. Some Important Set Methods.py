# Set Methods:

a = {'Sagar', 'Sonu', 'Edward', 'Jarvis'}
b = {'Edward', 'Golu', 'Vikky', 'Sunshile', 'Sonu'}

print("A:", a)
print("B:", b)
print()

ism = a.intersection(b) # same value display from both sets
print("Intersection Method: ", ism)
print()

i = a.union(b)
print(i)
print()

diff = a.difference(b)
print(diff)
print()

j = a.issubset(b)   # If both sets are same it returns True, if not it returns False
print(j)
print()

i = a.issuperset(b)
print(i)
print()




