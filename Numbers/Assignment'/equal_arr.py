#WAP Check if Two Arrays Are Equal
def equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    return sorted(arr1) == sorted(arr2)

arr1 = [1, 2, 3]
arr2 = [3, 2, 1]
print(equal(arr1, arr2))