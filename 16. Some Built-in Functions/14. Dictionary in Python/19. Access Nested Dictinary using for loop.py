# Accessing nested dictionary using for loop
a = {'course': 'Python', 'fees': 50000, 1: {'course':'java','fees':100000}}

# Accessing each id keys -- value
for i in a:
    if type(a[i]) is dict:
        for k in a[i]:
            print(k, "=", a[i][k])
    else:
        print(i, "=", a[i])
