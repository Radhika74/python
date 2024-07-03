#create class
class Person():
  name = "Neha"
  Occupation = "Software Engineer"
  networth = 100000
  def info(self):
    print(f"{self.name} is a {self.Occupation}")
a = Person() #object creation
b = Person()
c = Person()
a.name = "Radha"
a.Occupation = "Accountant"
b.name = "Rohan"
b.Occupation = "HR"
# print(a.name,a.Occupation)
a.info()
b.info()
c.info()
