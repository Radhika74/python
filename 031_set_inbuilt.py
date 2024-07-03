#inbuilt methods in sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print("union:",cities3)
cities4 = cities.intersection(cities2)
print("intersection:",cities4)
cities5 = cities.symmetric_difference(cities2)
print("symmetric_difference:",cities5)
cities6 = cities.difference(cities2)
print("difference:",cities6)
cities7 = cities.isdisjoint(cities2)
print("isdisjoint:",cities7)
cities8 = cities.issuperset(cities2)
print("issuperset:",cities8)
cities9 = cities.issubset(cities2)
print("issubset:",cities9)
cities10 = cities.add("Helsinki")
print("add:",cities10)
cities11 = cities.remove("Tokyo")
print("remove:",cities11)
cities12 = cities.discard("Tokyo")
print("discard:",cities12)
cities13 = cities.pop()
print("pop:",cities13)
cities14 = cities.clear()
print("clear:",cities14) #clear the elements 
cities15 = cities.update(cities2)
print("update:",cities15)
cities16 = cities.copy()
print("copy:",cities16)
cities17 = cities.clear()
print("clear:",cities17)
del cities
print(cities) #delete whole city so error name

