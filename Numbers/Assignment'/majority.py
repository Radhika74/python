def majorityElement(nums):
      sol = None
      cnt = 0
      for i in nums:
         if cnt == 0:
               sol = i
         cnt += (1 if i == sol else -1)
      return sol

nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(majorityElement(nums))
