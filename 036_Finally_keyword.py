#finally keyword is used to execute the code irrespective of the code is executed or not
def func1():
   try:
      l = [1,5,6,7]
      i = int(input("Enter the index: "))
      print(l[i])
      return 1
   except:
      print("some error occurred)")
      return 0
   
   finally:
      print("I am always executed")


x = func1()
print(x)
'''betterly used in function, file cleanup, close file ,data server connection where it is needed to execute compulsory as other part may not execute'''
   