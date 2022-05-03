# Copy() method is used to copy existing set's element into another set.
# Syntax: new_set_name = set_Name.copy()
#####################
# 1
a = {10, 20, "Edward"}
print("Before Copy:",a, id(a))
new_a = a.copy()
print("After Copy:", new_a, id(new_a))