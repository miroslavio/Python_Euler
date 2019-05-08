# Find sum of all primes below 2 million
import math

def is_prime(x): 
    if x < 2:
        return False
    if x < 4:
        return True # 2 and 3 are prime
    if x%2 == 0:
        return False # except for 2 all primes are odd
    lim = int(math.sqrt(x))
    for i in range(2, lim+1):
        if x%i == 0:
            return False
    return True

def brute_force(): # Way too slow!
    total_sum = 2
    
    num = 3
    limit = int(2e6)
    while num < limit:
        if is_prime(num):
            total_sum += num
        num += 2 # stick to odds

    print(total_sum)

brute_force()
    

