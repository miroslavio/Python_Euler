# Find product of coefficients a and b that produce the largest number of primes
# Can be sped up by only considering primes for values of b, since if b is not prime
# then all generated numbers cannot be prime
from itertools import compress

def is_prime(n): 
    if n < 2:
        return False
    i = 2

    # Loop from 2 to int(sqrt(n))
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1

    return True

# Apply sieve of eratosthenes in range 0 to n
def sieve(n):
    # is_prime[i] = 1 means i is prime
    is_prime = [1]*n

    # 0 and 1 are composites
    is_prime[0] = 0
    is_prime[1] = 0

    # Cross out all composites from 2 to sqrt(n)
    i = 2
    # Loop from 2 to int(sqrt         (n))
    while i*i <= n:
        # If we already crossed out the number then continue
        if is_prime[i] == 0:
            i += 1
            continue

        j = 2*i
        while j < n:
            # Cross out as it is composite
            is_prime[j] = 0
            # j is incremented by i
            j += i

        i += 1
    
    return list(compress(range(n+1), is_prime))

"""
We know:
1.) b must be prime to always satisfy n = 0
2.) use sieve of eratosthenes to generate prime numbers for b
3.) a must be odd
4.) a > -(n*n+b)/n for result to be positive
"""

b_vals = sieve(1000) # generate primes up to 1000
print(b_vals)
n = 1 # starting value, know it will always be prime for n = 0
largest_n = 0
final_a = 0
final_b = 0

for b in b_vals:
    for a in range(-999, 1000, 2): # Skip over even a values
        while is_prime(n*n + a*n + b):
            n += 1
        if n > largest_n:
            largest_n = n
            final_a = a
            final_b = b
        n = 1 # reset n

print("a=", final_a, " b=", final_b)
print(final_a*final_b)
