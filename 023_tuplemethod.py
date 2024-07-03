#methods of tuple 
tuple1=(1,2,3,4,5,6,7,8,9,10)
tuplex=()
print(tuple1)
 #use of loops for printing numbers
print("using loops")
for i in tuple1:
  print(i)

#use of methods
print("different Method of tuple")
print(len(tuple1))
print(max(tuple1))
print(min(tuple1))
print(sum(tuple1))
print(sorted(tuple1))
print(tuple1.index(2))
print(tuple1.count(2))
print(tuple1.index(2,3,6)) #start,stop,step
#not use these methods as tuple are immutable 
'''print(remove(tuple1))
print(count(tuple1,2))
print(tuple.range(tuple1,2,6))
print(tuplex.copy(tuple1))'''
