import math

# def count_divisors(n): # SLOW
#     for i in range(1, n):
#         if n%i == 0:
#             counter += 1
#     return counter

def count_divisors(n):
    divisor_count = 1
    factors = []
    counter = 1
    while n % 2 == 0: 
        counter += 1
        n = n / 2
        factors.append(2)
    divisor_count *= counter
    counter = 1 # reset
    
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2): 
        while n % i== 0:
            counter += 1
            n = n / i
            factors.append(i)
        divisor_count *= counter
        counter = 1
              
    # Condition if n is a prime 
    # number greater than 2 
        
    if len(factors) == 0: # rare instance of a prime
        return 2 # number itself and 1

    if n > 2: 
        factors.append(int(n))
        divisor_count *= (factors.count(n) + 1)
    
    return divisor_count


triangle_number = 1
nth_count = 1
required_divisors = 500
while count_divisors(triangle_number) < required_divisors:
    nth_count += 1
    triangle_number += nth_count

print("\nFinal triangle number: ", triangle_number)
