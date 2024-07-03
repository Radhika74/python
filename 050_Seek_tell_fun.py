with open("MyFile.txt","r") as f:
   print(type(f))
#move to the 10th byte in the file
   f.seek(10)
#read the next five bytes
print(f.tell())
data = f.read(5)
print(data)

