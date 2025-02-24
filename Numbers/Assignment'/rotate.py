def rotate_arr(arr, k):
    k %= len(arr)
    return arr[k:] + arr[:k]
    
arr = [1, 2, 3, 4, 5]
k=2
result=rotate_arr(arr, k)
print(result)