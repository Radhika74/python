l = [1, 2, 4, 6]
m = [8, 10, 12]

print("Original list l:", l)

# Append adds an element at the end
l.append(7)
print("After append(7):", l)

# Sort arranges the list in ascending order
l.sort()
print("After sort():", l)

# Reverse the list
l.reverse()
print("After reverse():", l)

# Return index of an element
print("Index of 1:", l.index(1))

# Count occurrences of an element
print("Count of 1:", l.count(1))

# Copy the list
l_copy = l.copy()
print("Copied list:", l_copy)

# Pop an element at a given index (removes and returns it)
popped_element = l.pop(2)
print("After pop(2), popped element:", popped_element)
print("List after pop:", l)

# Remove an element from the list
l.remove(1)
print("After remove(1):", l)

# Extend the list with another list
l.extend(m)
print("After extend(m):", l)

# Clear the list (removes all elements)
l.clear()
print("After clear():", l)

# Insert an element at a given index
l.insert(2, 3)  # This won't work properly since l is empty; inserting at index 2 will fail
print("After insert(2, 3):", l)

# Extend with three values
print("Extending with [8, 9, 10]:")
l.extend([8, 9, 10])
print("After extend([8,9,10]):", l)

# Copy list l to m
m = l.copy()
print("List m after copying list l:", m)

# Concatenation of lists
k = l + m
print("List k after concatenation of l and m:", k)
