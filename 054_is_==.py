a=4
b='4'
print(a is b) #exact location of object in memory
print(a==b) #exact value
c=(1,2,3)
d=(1,2,3)
print(c is d)
print(c==d)
a1=(3,4)
a2=(5,6,7)
print(a1 is a2)
print(a1==a2)
e=None
f=None
print(e is f)
print(e is None) # exact location of object in memory
print(e==f)
