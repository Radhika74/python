#Rotate the array taking user input
def rotate_array(arr, k):
    k = k % len(arr)
    arr[:] = arr[-k:] + arr[:-k]
    return arr

arr = list(map(int, input("Enter the array elements separate by space: ").split()))
k = int(input("Enter the number of positions to rotate: "))
print(rotate_array(arr, k))