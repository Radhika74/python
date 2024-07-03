class Person:
  #parameterized constructor
  def __init__(self,name,age): 
    self.name=name
    self.age=age
  def show(self):
    print(f"{self.name} is a {self.age}")

#default constructor
class Person1:
  def __init__(self):
    print("default constructor")

a=Person("Neha",18)
b=Person("Nikita",19)
c=Person1()
#error as three parameter 
#self is considered automatically
#c=Person(2,3,4) 
a.show()
b.show()

  