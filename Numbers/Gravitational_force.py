mass1 = float(input("First mass: "))
mass2 = float(input("Second mass: ")) 
r = float(input("Distance between the objects: "))
#how to write G as a constant
G = 6.673*(10**-11)
force =(G*mass1*mass2)/(r**2)
#round function round the value upto nearest integer value 
print("The gravitational force is:", 
round(force, 5),"N")
