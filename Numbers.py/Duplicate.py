#to find duplicate numbers frommlist
list1 = [2,44,2,6,8,9,2,4,5,6,7,8,9,10,11,12,13,]
list2 = []
for i in list1:
  if i not in list2:
    list2.append(i)
  else:
    print(i)

print(list2)
