def get_largest(nums):
   largest = nums[0]
   for num in nums:
       if num > largest:
           largest = num
   return largest
 
my_nums = [0,15,68,1,0,-55]
 
largest = get_largest(my_nums)
 
print('The largest number is: ', largest)


#another shortcut
'''nums = [41, 69, 23, 45, 19, 8]

largest = max(nums)
print(largest)
'''