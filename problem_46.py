import sieve

# Composites in the list are marked as zero
primes = sieve.sieve(1000000)

# Main body of the problem, find how to break n into a prime and remainder
# The remainder must be even, otherwise cannot be 2*square
def check_conjecture(n):
    i = 1
    while 2*i*i + 2 < n:
        square = i*i
        if primes[n - 2*square] == 1: # is prime that conjecture true
            return True
        i += 1
    return False

# Go over all odd composites
for i in range(9, len(primes), 2):
    if primes[i] == 1: # not composite, skip
        continue    
    if check_conjecture(i) == False:
        print("\nAnswer: ", i)
        break
        
    
