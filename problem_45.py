import math

def is_pent( n ): 
    n = (1 + math.sqrt(24 * n + 1)) / 6
    return( (n - int (n)) == 0) 

n = 143
while True:
    n += 1
    number = 2*n*n - n
    if is_pent(number):
        print("\nAnswer: ", number)
        break
