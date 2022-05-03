def show(d):
    print(d)
    print(type(d))
    for k in d:
         print(k, "=", d[k])

dc = {101:'Edward', 102:'Jarvis', 103:'Stark'}
show(dc)