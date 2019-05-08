import sieve
import timing

# Using indexing greatly improves performance
primes = sieve.sieve(1000000)

def trunc(n):
    r_trunc = n
    l_trunc = 0
    multiplier = 1
    while r_trunc > 0:
        l_trunc += multiplier * (r_trunc % 10)
        if  primes[r_trunc] == 0 or primes[l_trunc] == 0:
            return False
        r_trunc //= 10
        multiplier *= 10

    return True

# There are only 11 truncatable primes
count_ = 0
total = 0
while count_ < 10:
    for num in range(23, len(primes), 2):
        if trunc(num):
            print(num)
            total += num
            count_ += 1

print("\nAnswer: ", total)


timing.endlog()
