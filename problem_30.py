# Must determine a limit beyond which no number can be written as sum of its digits to the fifth power

def power_sum(n):
    sum_ = 0
    while n:
        sum_ += (n%10)**5
        n //= 10
    return sum_
    
min_ = 1000
max_ = 6*(9**5)

total_sum = 0
for i in range(min_, max_ + 1):
    if i == power_sum(i):
        print(i)
        total_sum += i

print("\nAnswer: ", total_sum)
