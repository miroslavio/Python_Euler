import sieve
limit = 1000000
primes = sieve.sieve(limit)

# Create a list of consecutive sums of all primes up to one million
consec = [0]

for i in range(2, len(primes)):
    if primes[i] == 1: # it is a prime number
        temp = i + consec[-1]
        if temp > limit*10:
            break
        consec.append(temp)
# consec = consec[1:] # Remove zero from the start
print(consec)

# Index position in consec tells us how many primes are used to get that consec sum
# If want a consec sum from a starting position other than i = 0, then need to subtract the value
# preceeding the start position
# Adopt a method that works for lim = 100, must return 41 with 6 primes in the sum
answer = 0
max_consec = 0
for i in range(len(consec) - 1):
    for j in range(i + 1, len(consec)):
        consec_sum = consec[j] - consec[i]
        if consec_sum >= limit:
            break
        if primes[consec_sum] == 1:
            length = j - i
        if length > max_consec:
            max_consec = length
            answer = consec_sum

print("\nAnswer: ", answer)
