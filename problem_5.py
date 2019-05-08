# Find the first natural number that is divisible by all numbers from 1 to 20
# The number must clearly be even, so SKIP ALL ODD NUMBERS.
# The number must be a multiple of 10, so check for N % 10 == 0

# Start with brute force
def brute_force():
    number = 20
    div = 2

    while div < 21:
        if number%div == 0:
            div += 1
        else:
            number += 1 # Keep going
            div = 2 # Reset

    print(number)

def faster_solution():
    start_num = 2520 # Simply use information from the problem
    div = 19 # we will check all numbers that are divisible by 20

    while div > 2: # we know for a fact that it will divide by 2 as its even
        if start_num % div != 0:
            start_num += 20 # Must be a multiple of 20
            div = 19 # Reset
        else:
            div -= 1

    # If the while condition is reached, then we found our number
    print(start_num)

    
def faster_solution2():
    # This is faster than above solutions as it exploits the math of finding
    # LCM of set of integers by multiplying their common prime factors
    integer_set = range(1, 21)
    for num in integer_set:
        
    
#brute_force() # FAR TOO SLOW
faster_solution() # Still quite slow
