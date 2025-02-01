cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

# Union (returns a new set)
cities3 = cities.union(cities2)
print("Union:", cities3)

# Intersection (returns a new set)
cities4 = cities.intersection(cities2)
print("Intersection:", cities4)

# Symmetric Difference (returns a new set)
cities5 = cities.symmetric_difference(cities2)
print("Symmetric Difference:", cities5)

# Difference (returns a new set)
cities6 = cities.difference(cities2)
print("Difference:", cities6)

# isdisjoint (returns True if sets have no common elements)
cities7 = cities.isdisjoint(cities2)
print("Is Disjoint:", cities7)

# issuperset (returns True if cities contains all elements of cities2)
cities8 = cities.issuperset(cities2)
print("Is Superset:", cities8)

# issubset (returns True if cities is a subset of cities2)
cities9 = cities.issubset(cities2)
print("Is Subset:", cities9)

# add() modifies the set in place (returns None)
cities.add("Helsinki")
print("After add('Helsinki'):", cities)

# remove() modifies the set in place (returns None)
cities.remove("Tokyo")  # Raises an error if element is not found
print("After remove('Tokyo'):", cities)

# discard() modifies the set in place (returns None, but avoids error if element is missing)
cities.discard("Tokyo")
print("After discard('Tokyo'):", cities)

# pop() removes and returns a random element
popped_element = cities.pop()
print("After pop(), removed element:", popped_element)
print("After pop(), cities:", cities)

# clear() removes all elements (modifies set in place)
cities.clear()
print("After clear():", cities)

# update() modifies the set in place (returns None)
cities.update(cities2)
print("After update(cities2):", cities)

# copy() returns a new set
cities16 = cities.copy()
print("Copy of cities:", cities16)

# clear() again to empty the set
cities.clear()
print("After second clear():", cities)

# del deletes the set entirely
del cities

# Attempting to print `cities` after deletion will cause an error
try:
    print(cities)
except NameError:
    print("Error: 'cities' is deleted and no longer exists.")
