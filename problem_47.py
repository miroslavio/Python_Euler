import math

def prime_factors(n):
    '''Find unique prime factors of n'''
    factors = []
    
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2
            
    # n must be odd at this point, so use this in your loop
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i

    # Condition to handle the case when n is prime greater than 2
    if n > 2:
        factors.append(n)

    return factors

n = 647
count = 0
while True:
    n += 1
    for i in range(n, n+4):
        if len(prime_factors(i)) == 4:
            count += 1
        else:
            count = 0 # reset
            break
    if count == 4:
        break

if count == 4:
    print("Answer: ", n)
        
