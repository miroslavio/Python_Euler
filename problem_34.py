# Find an appropriate limit
# Number such as abcd = a! + b! + c! + d!
# Take abc = 145, 1! + 4! + 5! = 145
import math

def digit_factorial(n):
    sum_ = 0
    temp = n
    while n:
        sum_ += math.factorial(n % 10)
        n //= 10
    
    if sum_ == temp:
        return True
    else:
        return False

for i in range(3, 1000000):
    if digit_factorial(i):
        print(i)
