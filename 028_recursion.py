def fibonacci_series(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    
    series = []
    a, b = 0, 1
    
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    
    return series

n = int(input("Enter the number of terms in the Fibonacci series: "))
print("Fibonacci series:", fibonacci_series(n))
