def get_second_smallest(nums):
   smallest = float('inf')
   second_smallest = float('inf')
   for i in range(0,len(nums)):
       if nums[i] <= smallest:
           second_smallest = smallest
           smallest = nums[i]
       elif nums[i] < second_smallest:
           second_smallest = nums[i]
   return second_smallest
 
my_nums = [44,11,83,29,25,76,88]
second_smallest = get_second_smallest(my_nums)
print("Second smallest number is : ", second_smallest)
#inf is used to represent infinity 
