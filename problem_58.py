import math as m

def is_prime(n):
    if n < 2:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = int(m.sqrt(n))
        f = 5
        while f <= r:
            if n%f == 0:
                return False
            if n%(f+2) == 0:
                return False
            f += 6
        return True

# Variable n refers to the length of the spiral
n = 3
num_primes = 3
ratio = num_primes / (2*n - 1)
while ratio > 0.1: #stop when goes below 10%
    n += 2
    for a in range(1, 4):
        if is_prime(n*n - a*(n-1)):
            num_primes += 1
    # Numbers in diagonals is 2*n - 1
    ratio = num_primes / (2*n - 1)

print("\nAnswer: ", n)
