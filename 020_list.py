list1=[1,2,3,4,5,6]
list2=[7,8,9,10]
print(list1)
print(list2)
print(list1[0])
print(type(list1))

#for negative index access value
print(list1[-2])
print(list1[len(list1)-2])
print(list1[5-2])
print(list1[3])

#jump index
print("Jump index example ")
print("original list",list1)
print("No values" ,list1[:])
print("left value assign",list[1:])
print("right value assign",list1[:5])
print("Two value are given",list1[1:5])
print("three values are given",list[1:6:2])
print("negative index",list1[1:4:-2])


#list1 is assigned a list of numbers from 1 to 6
list1 = [1, 2, 3, 4, 5, 6]
# list2 is assigned a list of numbers from 7 to 10
list2 = [7, 8, 9, 10]

# Print the elements of list1 and list2 on separate lines
print(list1)
print(list2)

# Print the first element of list1
print(list1[0])

# Print the data type of list1 
print(type(list1))

# Print the value at index -2 (second last element) in list1 
print(list1[-2]) 

# This line is equivalent to the line above 
print(list1[len(list1)-2])

# Accessing element at index 3 (which is 4) in list1
print(list1[3])

# Jump index example
print("Jump index example ")

# Print the original list
print("original list", list1)

# Print a slice of list1 containing all elements (equivalent to printing the entire list) 
print("No values", list1[:])

# Trying to assign a value to list1 using slicing is not possible because lists are immutable
# print("left value assign", list[1:])  # This line is incorrect

# Accessing element at index 5 (which is 6)  out of bounds will cause an error 
print("right value assign", list1[5]) 
# This line causes an error 

# Print a slice of list1 containing elements from index 1 (inclusive) to 5 (exclusive) 
print("Two value are given", list1[1:5])

# Print a slice of list1 containing elements at index 1 (inclusive), 3 (exclusively)

print("negative index", list1[1:4:-2])



