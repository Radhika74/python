#Generator have on the fly have value 
#different from list

def my_generator():
    for i in range(50000):
        yield i
      
gen = my_generator()
gen1 = my_generator()
print(next(gen)) #0
print(next(gen)) #1
print(next(gen)) #2
print(next(gen)) #3
print(next(gen)) #4
#alternative
for j in gen1:
  print(j)