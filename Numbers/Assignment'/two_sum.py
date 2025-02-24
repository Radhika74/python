#Two Sum Problem
def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
nums = list(map(int, input("Enter array separate by space: ").split()))
target = int(input("Enter target: "))
print(twosum(nums, target))