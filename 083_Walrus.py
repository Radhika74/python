foods = list()
#walrus : direct assigning value to variable
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)