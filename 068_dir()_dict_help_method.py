#use of dir() method
x = [2,3,4]
print(dir(x))
print(x.__add__)

#use of help() method
print(help(x.append))
print(str())

#use of dict() method
class Parents:
  def __init__(self,name,age):
    self.name=name
    self.age=age

a = Parents("Radha",18)
print(a.__dict__)

  
