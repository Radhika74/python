#custom errors stop the program that is unexpected 
#raise keyword is used to raise custom errors

a=int(input("Enter any value between 5 and 9: "))
if(a<5 or a>9):
  raise ValueError("Value should be between 5 and 9")
  
#defining custom exception using class
#class CustomError(Exception)

