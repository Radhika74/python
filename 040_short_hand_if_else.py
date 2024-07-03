#example of short hand if else


a=330
b=3303
print("A") if a>b else print("=") if a==b else print("B")
print("9" if a<b else"")
c=9 if a>b else 0
print(c)

#another example
condition = True  # Example condition
value_if_true = "Condition is True"
value_if_false = "Condition is False"

result = value_if_true if condition else value_if_false
print(result)
