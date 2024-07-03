#using loops 
print("using loops")
for i in range(5):
  print(i)

print("using loops with range")
for i in range(1,6):
  print(i)

print("using loops with range and increment")
for i in range(1,6,2):
  print(i)

print("using loops with range and decrement")
for i in range(5,0,-1) #start,stop,step
  print(i)

#Using while loop
print("using while loop")
i=0
while i<5:
  print(i)
  i=i+1

#using while loop with else
print("using while loop with else")
i=0
while i<5:
  print(i)
  i=i+1
  if i==3:
    break
  else:
      print("loop is finished")


  
