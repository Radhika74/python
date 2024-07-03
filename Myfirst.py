def welcome():
  print("Hey,You are welcomed")

print(__name__)
if __name__ == "__Myfirst__": 
  # __name__ is a built in variable in python.
  # It is used to check whether the current module is being execute
  # directly or being imported.
  # If the current module is being executed directly, then it will
  # have a name "__main__".
  # If the current module is being imported, then it will have a name
  # equal to the name of the module being imported.
  
  welcome()
  
  '''basically we are using it to tell from where i am running the code and if i am running the code from main.py then it will run the welcome function and if i am running the code from another file then it will not run the welcome function'''

