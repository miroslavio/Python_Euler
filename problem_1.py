# Find sum of all multiples of 3 and 5 below 1000

def is_multiple(x):
    if x%3==0 or x%5==0:
        return True
    else:
        return False

total_sum = 0 # This will be the final answer
number = 1

while number < 1000:
    if is_multiple(number):
        total_sum += number
    number += 1

print(total_sum)
