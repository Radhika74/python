s = {1, 2, 5, 6}
s2 = {3, 6, 7}

# Union of two sets
print("After performing union:", s.union(s2))

# Intersection of two sets
print("After performing intersection:", s.intersection(s2))

# Update the set with another set (adds elements from s2 to s)
s.update(s2)
print("After update s with s2:", s)

# Intersection update (modifies s to keep only common elements)
s.intersection_update(s2)
print("After intersection update:", s)

# Symmetric difference (returns elements not common in both sets)
sym_diff = s.symmetric_difference(s2)
print("Symmetric difference:", sym_diff)

# Symmetric difference update (modifies s to keep only non-common elements)
s.symmetric_difference_update(s2)
print("After symmetric difference update:", s)

# Difference (returns elements in s but not in s2)
diff = s.difference(s2)
print("Difference:", diff)

# Difference update (removes elements of s2 from s)
s.difference_update(s2)
print("After difference update:", s)
