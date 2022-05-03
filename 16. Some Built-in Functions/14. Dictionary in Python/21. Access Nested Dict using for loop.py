a = {1: {'course': 'Python', 'fees': 50000},
     2: {'course': 'java', 'fees': 100000}}

# finding id (key) using loop
print("Id")
for id in a:
    print(id)
print()
# keys under id(key)
print("Keys:")
for id in a:
    for k in a[id]:
        print(k)
print()
#
# Access key-value
for id in a:
    for k in a[id]:
        print(k,"=", a[id][k])
