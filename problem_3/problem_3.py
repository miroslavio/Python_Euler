from math import sqrt
# Find largest prime factor of 600851475143
number = 600851475143

# Simple function to test if x is prime
def is_prime(x):
    n = 2
    while n <= sqrt(x):
        if x%n == 0:
            return False
        n += 1
    return True

# SOLUTION:
# Find the highest number that is divisible yet is also a prime
# ISSUE: number is very large so efficient solution must be found
# Generate prime numbers from sqrt(number), then test if any is a factor
# the first factor should be the answer.
test_num = round(sqrt(number))

# First find a large factor
while True:
    if number % test_num == 0:
        if is_prime(test_num):
            print(test_num)
            break
    test_num -= 1
