#DICTIONARY METHODS
d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))
print(d.get(1))
print(d.get((1, 2)))

# Accessing non-existent key
print(d.get("age"))

# Updating value using key
d["name"] = "Bob"
print(d["name"])

# Updating value using setdefault()
d.setdefault("age", 30)
print(d["age"])

# Updating value using update()
d.update({"city": "New York"})
print(d["city"])

# Adding a new key-value pair
d["country"] = "USA"
print(d["country"])

# Removing a key-value pair using pop()
d.pop("age")
print(d)

# Removing a key-value pair using popitem()
d.popitem()
print(d)

# Removing all key-value pairs using clear()
d.clear()
print(d)

# Checking if a key exists in the dictionary
print("name" in d)
print("age" in d)
print((1, 2) in d[(1, 2)])

# Getting all keys
print(d.keys())

# Getting all values
print(d.values())

# Getting all key-value pairs
print(d.items())