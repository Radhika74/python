tup=(1,2,76,342,32,'green',True)
tup2=tup[1:4]
print(tup2)
print(tup[1:4])
print(tup[1:4:2])
print(tup[:3])
print(tup[1:])
print(tup[:])
print(tup[::2])
tup3=("spain","italy","india","England ","Germany")
temp=list(tup3)
temp.pop(3)
tup3=tuple(temp)
print(tup3)