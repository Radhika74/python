a=int(input("Enter age:"))
if (a>18):
   print("You can drive")
else:
   print("You cannot drive")
   print("not permitted ")
print("yay!!\n")   #example of indentation

#another 
print("another example Of Loops")
applePrice=210
budget=200
if(applePrice<=budget):
   print("Alexa, add 1 kg Apples to the cart.")
else:
   print("Alexa, do not add Apples to the cart.\n")

#use of elif
print("use of if elif else")
a1=10
a2=200
if(a2-a1>50):
   print("You can buy")
elif(a2-a1>70):
   print("okh, buy")
else:
   print("You can't buy\n")

#nested if
print("\n nested if example ")
num=18
if(num<0):
   print("negative ")
elif(num>0):
   if(num<=10):
      print(num,"is between 1-10")
   elif(num>10 and num<=20):
      print(num,"is between 11-20")
   else:
      print(num,"is greater than 20")
else:
   print("number is zero\n")