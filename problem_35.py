import itertools

# Generate prime numbers up to n
def sieve(n):
    # is_prime[i] = 1 means i is prime
    is_prime = [1]*n

    # 0 and 1 are composites
    is_prime[0] = 0
    is_prime[1] = 0

    # Cross out all composites from 2 to sqrt(n)
    i = 2
    # Loop from 2 to int(sqrt(n))
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
    
    return list(itertools.compress(range(n+1), is_prime))

# Prime numbers
primes = sieve(1000000)

# Where n is a prime
def cyclic(n):
    if n < 10:
        return True # all single digit primes are cyclic
    n_digits = []
    while n:
        digit = n % 10
        if digit % 2 == 0 or digit == 5:
            return False # cannot ever be a cyclic prime if it contains an even digit or a 5
        n_digits.insert(0, digit)
        n //= 10
    # Generate rotations of n and ask if the new rotation is prime
    for i in range(len(n_digits) - 1): # -1 so the original rotation is not repeated
        n_digits.append(n_digits.pop(0)) # Rotate
        number = 0
        factor = 1
        for j in n_digits[::-1]:
            number += factor*j
            factor *= 10
        if number not in primes:
            return False
        
    return True
     
cyclic_primes = [] 

for i in primes:
    if cyclic(i):
        cyclic_primes.append(i)

print(len(cyclic_primes))
