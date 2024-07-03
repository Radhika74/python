#MAP
#def cube():
 # return x * x * x
#print(cube(2))
l = [1, 2, 4, 6, 4, 3]
#newl = []
#forr item in l:
  #newl.append(cube(item))
newl = list(map(lambda x: x*x*x, l))
print(newl)

