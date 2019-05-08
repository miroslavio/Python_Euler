import math

def sum_divisors(number):
    if number < 2:
        return 0 # 1 has no divisors
    
    limit = int(math.sqrt(number))
    divisor_sum = 1 # 1 is counted always
    if limit*limit == number: # special case for perfect square numbers
        divisor_sum += limit
    else:
        limit += 1
    for n in range(2, limit):
        if number % n == 0: # Found a divisor
            divisor_sum += n
            divisor_sum += number//n # divisors always come in pairs
            
    return divisor_sum

def is_abundant(number):
    if number % 2 != 0 and number % 3 != 0: 
        return False # true up to well beyond our limit
    if sum_divisors(number) > number:
        return True
    else:
        return False

def condition(n): # n not possible to express as sum of two abundant numbers
    for i in range(12, n//2 + 1): # Start from smallest abundant number
        if is_abundant(i) and is_abundant(n-i):
            return False
    return True

# CONDITION: n = a+b where a,b are abundant numbers, sum all n that do not meet this
limit = 20161 # From wikipedia
total_sum = sum(range(1,24)) # first 23 numbers cannot be sum of two abundants
numbers = list(range(24, limit+1)) # all possible integers in range of CONDITION

for num in numbers:
    if condition(num):
        total_sum += num

print(total_sum)

# # TESTING
# abun_numbers = []
# for i in range(1,100):
#     if is_abundant(i):
#         abun_numbers.append(i)

# print("List of abundant numbers:\n", abun_numbers)

# condition_numbers = []
# for i in range(1,100):
#     if condition(i):
#         condition_numbers.append(i)

# print("\nNumbers that meet the condition:\n", condition_numbers)


