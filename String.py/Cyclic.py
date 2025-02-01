def are_cyclic(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

# Input
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Output
if are_cyclic(s1, s2):
    print("Strings are cyclic")
else:
    print("Strings are not cyclic")
