class Solution:
    def subsetXORSum(self, nums):
        total = 0
        for num in nums:
            total |= num  
        return total * (1 << (len(nums) - 1))

solution = Solution()
result = solution.subsetXORSum([1, 2, 3])
print(result)
    