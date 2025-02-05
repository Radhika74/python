#find frequency of each no. of the array
def find_frequency(arr):
    freq_dict = {}
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    return freq_dict

arr=input()
freq_dict = find_frequency(arr)
print(freq_dict)