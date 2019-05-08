# Find 10,001st prime number
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

# How to get nth prime number? No formula like that exists.
counter = 0 # Increment by 1 for every prime number found
num = 1 # This variable will store the final answer

while counter < 10001:
    num += 1
    if is_prime(num):
        counter += 1

print(num)
