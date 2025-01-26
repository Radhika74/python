var1 = '45'
var2 = '49'

# String concatenation
print(var1 + var2)

# Convert strings to integers and add
print(int(var1) + int(var2))

# Convert strings to floats and add
print(float(var1) + float(var2))

# Explicitly concatenate strings
print(str(var1) + str(var2))

# More examples of implicit type casting
a = 5
b = 5.5
print(a + b)  # int + float -> float
print(type(a))
print(type(b))
print(type(a + b))

# More examples of explicit type casting
a1 = 5
b1 = 5.5

# Convert int to float
print("Explicit conversion: int to float")
print(float(a1))
print("Value of a1 after explicit typecasting:", type(float(a1)))

# Convert float to int
print("Explicit conversion: float to int")
print(int(b1))
print("Value of b1 after explicit typecasting:", type(int(b1)))

# Convert int to string
print("Explicit conversion: int to string")
print(str(a1))
print("Value of a1 after explicit typecasting:", type(str(a1)))

# Convert string to int
print("Explicit conversion: string to int")
print(int(float(b1)))  # Convert string to float first, then to int
print("Value of b1 after explicit typecasting:", type(int(float(b1))))

# Convert float to string
print("Explicit conversion: float to string")
print(str(b1))
print("Value of b1 after explicit typecasting:", type(str(b1)))

# Boolean conversions
print(bool(a1))  # Non-zero int -> True
print(bool(b1))  # Non-zero float -> True
print("Value of a1 after explicit typecasting:", type(bool(a1)))
print("Value of b1 after explicit typecasting:", type(bool(b1)))

# Boolean to int and float
print("Boolean values to int & float:")
print(int(True))  # True -> 1
print(int(False))  # False -> 0
print(float(True))  # True -> 1.0
print(float(False))  # False -> 0.0

# Boolean to string
print("Boolean values to string:")
print(str(True))  # True -> 'True'
print(str(False))  # False -> 'False'
