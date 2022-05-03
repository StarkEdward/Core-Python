# Membership Operator
# in
st1 = "King in the North"
print("the" in st1)

st2 = "King in thes North"
print(("the" in st2))

st3 = "King in the North"
print("stark" in st3)

st4 = "Welcome to the Starks Industry"
print("ar" in st4)

st5 = "Welcome to the Starks Industry"
print("art" in st5)

list = ["Goa", "Stark", "King in the North"]
print("Goa" in list)

tup = ("dragon", 10, 25, "sonu")
print(10 in tup)

# not in
st1 = "Welcome to North"
print("got" not in st1)

st2 = "Welcome to North"
print("to" not in st2)

st3 = "Welcome top North"
print("to" not in st3)

list = ["Goa", "Stark", "King in the North"]
print("Hut" not in list)

list = ["Goa", "Stark", "King in the North"]
print("Stark" not in list)

tup = ("dragon", 10, 25, "sonu")
print(10 not in tup)

tup = ("dragon", 10, 25, "sonu")
print(100 not in tup)
