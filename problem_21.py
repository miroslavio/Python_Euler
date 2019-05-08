import math

def sum_divisors(number):
    limit = int(math.sqrt(number)) + 1
    if number < 2:
        return 0 # 1 has no divisors
    divisor_sum = 1 # 1 is counted always
    for n in range(2, limit):
        if number % n == 0: # Found a divisor
            divisor_sum += n
            divisor_sum += number//n # divisors always come in pairs
    return divisor_sum

def is_amicable(a):
    b = sum_divisors(a)
    if sum_divisors(b) == a and b != a:
        return True
    else:
        return False

# Sum all numbers below 10000 for which is_amicable is True
total = 0
limit = 10000
for i in range(1, limit):
    if is_amicable(i):
        print(i)
        total += i

print(total)

