#Built file handling methods binary + txt file
#file name, mode, encoding 
#r to read only ,it can be default if not written 

f = open("MyFile.txt",'r')
#print(f)
print(f.read()) #for reading file
print(f.close()) #close file 
#to write in file if not exist then it will create the file
f = open("MyFile.txt",'w')
txt=f.write("hello world")
print(txt)
print(f.close())
#to write in file at end and content remained same 
#to append file

#using with automatically closed the open file
with  open("MyFile.txt",'a') as f:
  (f.write("hello"))

