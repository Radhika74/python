#using if statement 
a=5
b=6
if a>b:
  print("a is greater than b")

print("b is greater than a")
 #using if else statement
if a>b:
  print("a is greater than b")
else:
  print("b is greater than a")
  #using elif statement
  a1=56
  b1=55
  if a1>b1:
    print("a1 is greater than b1")
  elif a1==b1:
      print("a1 is equal to b1")
  else:
      print("b1 is greater than a1")

  #using nested if statement
  a2=int(input("Enter first number: "))
  b2=int(input("Enter second number: "))
  if a2>b2:
    print("a2 is greater than b2")
    if a2==b2:
      print("a2 is equal to b2")
    else:
      print("b2 is greater than a2")
  else:
    print("b2 is greater than a2")
    if a2==b2:
      print("a2 is equal to b2")
    else:
      print("a2 is greater than b2")
      
 