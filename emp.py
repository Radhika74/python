class Employee:
  def __init__(self,name,):
    self.name = name
  def __len__(self):
    i=0
    for c in self.name:
      i=i+1
    return i
  
#str is used to convert object to string toprint string
  def __str__(self):
    return f"The name of the employee is{self.name} str"
#repr is used to convert object to string to get string representation 
  def __repr__(self):
   return f"Employee name: {self.name} repr"
  def __call__(self):
   print("hey I am Good")
    
    