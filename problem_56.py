def sum_digits(n):
    sum_ = 0
    while n:
        sum_ += n%10
        n //= 10
    return sum_

max_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        sum_ = sum_digits(a**b)
        if sum_ > max_sum:
            max_sum = sum_

print("\nAnswer: ", max_sum)
