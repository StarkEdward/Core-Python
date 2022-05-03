# Passing and Returning Dictionary.
def show(d):
    print(d)
    print(type(d))
    for k in d:
        print(k, "=", d[k])
    return d


dc = {101: 'Edward', 102: 'Jarvis', 103: 'Stark'}
new_dc = show(dc)
print(new_dc)
print(type(new_dc))
