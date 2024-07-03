class Employee:
   def __init__(self, name, age, salary):
      self.name = name
      self.age = age
      self.salary = salary
   def display(self):
      print(self.name, self.age, self.salary)
class Programmer(Employee):
   def showlanguage(self):
     print("This is python")
  
emp1 = Employee('Radha', 18, 10000)
emp2 = Employee('Ram', 19, 20000)
emp1.display()
emp2.display()
emp3 = Programmer('Raj', 20, 30000)
emp3.display()
emp3.showlanguage()

