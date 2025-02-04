class Employee:
  #class variable
    company = "Google"
    def __init__(self,name):
      #instance variable
      self.name = name
      self.raise_amount = 0.02
    def showDetails(self):
      print(f"The name of the employee is {self.name} and the company is {self.company}")
emp1 = Employee("Radha")
emp1.raise_amount = 0.34
emp1.company = "Apple"
emp1.showDetails()
emp2 = Employee("Ram")
emp2.company = "Microsoft"
emp2.showDetails()

  