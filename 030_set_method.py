s={1,2,5,6}
s2={3,6,7}
print("After performing union",s.union(s2)) #union of two sets
print("After performing intersection",s.intersection(s2)) #intersection of two sets
s.update(s2) #update the sets
print(s,s2)

s.intersection_update(s2) #intersection update of two sets
print(s,s2)
s.symmetric_difference(s2)
print(s,s2)
s.symmetric_difference_update(s2)
print(s,s2)
s.difference(s2)
print(s,s2)

s.diffe