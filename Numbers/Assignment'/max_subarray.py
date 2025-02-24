# Maximum subarray sum
def max_subarray_sum(arr):
    max_arr = arr[0]
    curr_max = arr[0]

    for i in range(1, len(arr)):
        curr_max = max(arr[i], curr_max + arr[i])
        max_arr = max(max_arr, curr_max)

    return max_arr

arr = list(map(int, input("Enter array separate by space: ").split()))
print(max_subarray_sum(arr))