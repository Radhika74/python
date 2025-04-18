class Solution(object):
    def countPairs(self, nums, k):
        pairs = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    pairs += 1
        return pairs
#call fun

nums = [1, 2,1,3,1,2,1,2,3,1,1,3, 3, 4, 5]
k = 2
sol = Solution()
result = sol.countPairs(nums, k)
print(result)
