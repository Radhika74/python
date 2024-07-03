#enumerate function 
#help to iterate list,string, tuple easily 
#tells index and value of list at same time 
marks=[12,56,32,98,12,45,1,4]
'''for marks in mark:
      print(marks)
      if (index==3):
       print("excellent")
       i+=1
'''
for index, mark in enumerate(marks):
    print(mark)
    if (index==3):
       print("excellent ")
  