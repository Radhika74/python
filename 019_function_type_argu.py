#functional arguments 
def average(a,b):
  print("The average is",(a+b/2))
average(4,6)
#default argument 
def name(fname,lname="John",mname="whatson"):
    print(fname,mname,lname)
name("Amyy")
#keyword argument 
def name1(fname,mname,lname):
  print(fname,mname,lname)
name1(mname="Peter",lname="Wesker",fname="Jade")
#required argument
def name2(fname,mname,lname):
  print(fname,mname,lname)
name2("Peter","Ego","Quill")
#variable length argument
def average1(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
      sum=sum+i

    print("Average is:",sum/len(numbers))

average (5,6)
#return statement
def average2(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
      sum=sum+i

    return sum/len(numbers)

c=average2(5,6,7,1)
print(c)


  

