#to calculate given no. is prime or not
def prime(n):
   for i in range(2,n):
    if n%i==0:
      return False
    return True
      
num = int(input("enter no."))
if_prime=prime(num)
if if_prime:
  print("prime")
else:
  print("not prime")
  
          