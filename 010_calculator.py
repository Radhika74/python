#creating calculator
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Addition of",a,"and",b,"is",a+b)
print("Subtraction of",a,"and",b,"is",a-b)
print("Multiplication of",a,"and",b,"is",a*b)
print("Division of",a,"and",b,"is",a/b)
print("Modulus of",a,"and",b,"is",a%b)
print("Floor Division of",a,"and",b,"is",a//b)
print("Exponential of",a,"and",b,"is",a**b)
#using binary operators
print("Binary AND of",a,"and",b,"is",a&b)
print("Binary OR of",a,"and",b,"is",a|b)
print("Binary XOR of",a,"and",b,"is",a^b)
print("Binary NOT of",a,"is",~a)
print("Binary NOT of",b,"is",~b)
print("Binary Left Shift of",a,"is",b<<a)
print("Binary Right Shift of",a,"is",b>>a)
print("Binary Right Shift of",b,"is",a>>b)
print("Binary Right Shift of",a,"is",a>>b)
#using assignment operators
a+=5
print("a after increment:",a)
a-=5
print("a after decrement:",a)
a*=5
print("a after multiplication:",a)
a/=5
print("a after division:",a)
a%=5
print("a after modulus:",a)
a//=5
print("a after floor division:",a)
a**=5
print("a after exponential:",a)
#error a&=5
print("a after binary AND: exception")
print("Thank you for using this calculator")
