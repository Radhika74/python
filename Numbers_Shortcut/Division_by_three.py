#print all the numbers divisible by 3 & 5 according to the number enter by user
num = int(input('Insert the number: '))
result = [] 
i = 1
while i<=num:
   if i%3==0 and i%5==0:
       result.append(i)
   i=i+1
 
print(result)