# method 1 : not used widely
a = range(6)
for i in a:
    print(i)

# method 2 most useful
# generating number from 0 to 4
for a in range(5):
    print(a)

# generate number from 1 to 9
for i in range(1, 10):  # start from 0 upto (10-1) = 9
    print(i)

# generate number from 0 to 10 with increment of 2
for i in range(0, 10, 2):   # increment 0 2 4 6 8
    print(i)

# generate negative number from -1 to -10 with increment -2
for i in range(-1, -10, -2):    # -1, -3 -5 -7 -9
    print(i)

# generate number from 10 to 0 with decrement -2
for i in range(10, 0, -2):      # 10 8 6 4 2
    print(i)

# genetrate table for 5 using for loop
n = 5
for i in range(1, 11):
    print(n,"x", i,"=", i*5)


# generating number upto users input
num = int(input("Enter number: "))
for i in range(1, num+1):    # start from 0 upto num-1
    print(i)

# generating char with index number using range function
st = "StarkJarvis"
n = len(st)
for i in range(n):
    print(i, "=", st[i])
# OR
st = "Stark Edward"
for ch in range(len(st)):
    print(f"{ch} = {st[ch]}")