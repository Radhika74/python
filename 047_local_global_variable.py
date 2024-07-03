x=5  #global variable 

#print(y) error not accessible as it is local vaiable

def my_function():
      x=10  #local variable 
      y = 20  #local variable
      global z
      z=30  #global variable
      print(x)
      print(y)

print(x)
'''print(y) error as y is local variable and call within function so not accessible in main program '''
my_function()
print(z)
