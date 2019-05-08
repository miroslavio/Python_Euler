import sieve

# Generate all needed primes for this problem
primes = sieve.sieve(100000)

def is_perm(a, b, c):
    '''Return True if a, b and c are permutations of one another'''
    d_a = [0]*10
    d_b = [0]*10
    d_c = [0]*10
    while a:
        d_a[a%10] += 1
        a //= 10
    while b:
        d_b[b%10] += 1
        b //= 10
    while c:
        d_c[c%10] += 1
        c //= 10

    return d_a == d_b == d_c

diff = 0
for i in range(1001, 9998, 2): # all primes>2 are odd
    if primes[i] == 1:
        for j in range(i + 2, 10000, 2):
            if primes[j] == 1:
                diff = j - i
                if primes[j + diff] == 1:
                    if is_perm(i, j, j + diff):
                        print(i, j, j + diff)
                        
