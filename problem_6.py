def sum_squared(n): # from 1 to n
    numbers = list(range(1, n+1)) #in v3 range is an iterator so convert
    return (sum(numbers))**2

def squared_sum(n):
    numbers = list(range(1, n+1))
    numbers = [i**2 for i in numbers] # Square each number
    return sum(numbers)

print(sum_squared(100) - squared_sum(100))
