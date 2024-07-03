#methods of list 
l=[1,2,4,6]
m=[8,10,12]
print(l)
#append add element at last of list
print(l.append(7)) 
#sort check the list in ascending order 
print(l.sort())
#reverse the list 
print(l.reverse())
#return index of element 
print(l.index(1))
#count the number of element given  
print(l.count(1))
#copy the list
print(l.copy())
#pop the element from list
print(l.pop(2))
#remove the elements from list
print(l.remove(1))
#extend the list 
print (l.extend(m))
#clear the list
print(l.clear())
#insert the element at given index
print(l.insert(2,3))  #at index,this value
#extend with three value 
print("extend example 8,9,10")
print(l.extend([8,9,10]))

m=l.copy()
print("list m after copy list l",m)
#concatenation
k=l+m
print("list k afte concatenation l and m list",k)