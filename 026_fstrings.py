letter= "Hey my name is {1} and I am from {0}"
country="India"
name="Whatson"
print(letter.format(country,name))
print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}")
price=49.09999
txt=f"For only {price:.2f} dollars!"
print(txt)
print(f"{2*30}")
print(type(f"{2*30}"))

