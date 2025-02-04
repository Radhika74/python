#Second largest element
def second_largest(numbers):
    first_largest = second_largest = float('-inf')
    for num in numbers:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num
    return second_largest

numbers = [3, 5, 1, 9, 7, 2, 6]
print(second_largest(numbers))