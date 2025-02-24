def duplicate(nums):
    res=[]
    n=set()
    for x in nums:
        if x in n:
            res.append(x)
        else:
            n.add(x)
    return res

nums = list(map(int, input("Enter array separate by space: ").split()))
print(duplicate(nums))