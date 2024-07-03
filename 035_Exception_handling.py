a=input("Enter the number:")
print(f"Multiplication table of{a} is:)")
'''Exception is used so our program can be successfully executed 
if we give any string value it will give error and stop the program 
so exception handling is used to handle the program without crushing '''
try:
     for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
  print(e)

print("some lines of code")
print("end of program")


#types of error here occur
#except ValueError:
#except IndexError: