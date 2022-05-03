print("%d" % 432)

print("%d %d" % (432, 345))

print("%f" % 432.123)

print("%f %f" % (432.45, 10.3))

print("%f" % 432.123456)

print("%f" % 432.12345651)

print("%f" % 432.12345641)

print("%s" %"Edward")

print("%s %s" % ("Stark", "Edward"))

print("%d %s" % (432, "Edward"))

#####################################################
# Without Maintain Order
print("%(nm)s %(ag)d"%{'ag':26, 'nm': "Jarvis"})
######################################################
# flag
print("%d" % 432)
print("% d" % 432)
print("%+d" % 432)
########################################################
# width include
print("%8d" % 432)
print("%08d" % 432)
print("%+8d" % 432)
#################################################
# precision
print("%f" % 432.123)
print("%.3f" % 432.123)
print("%.2f" % 432.123)
print("%.2f" % 432.128)
print("%9.2f" % 432.128)
print("%09.2f" % 432.123)
print("%+.2f" % 432.128)
#####################################################
#
print("My age is %d" % 26)
#
a = "Stark"
b = "Edwad"
print("Hello %s %s" %(a, b))
#
a = "Hello My age is %d" % 26
print(a)
