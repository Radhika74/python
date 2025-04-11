class Solution:
    def Operations(self, nums, k):
        st = set()
        for x in nums:
            if x < k:
                return -1
            elif x > k:
                st.add(x)
        return len(st)
nums =[2,3,6,7,9,9,7]
k = 5
sol = Solution()
result = sol.Operations(nums, k)
print(result)
