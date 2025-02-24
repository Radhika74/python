#Finding missing elements
def missingNumber(nums):
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        
        return res

nums = list(map(int, input("Enter array separate by space: ").split()))
print(missingNumber(nums))