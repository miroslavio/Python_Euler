def sieve(n):
    """Generate list of prime numbers up to n."""
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
    
    #return list(itertools.compress(range(n+1), is_prime))
    return is_prime # boolean list where index is the prime number
