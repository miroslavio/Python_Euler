import timing
import permutations

def is_pan(n):
    '''Return True if n is 1-9 pandigital'''
    digits = [0]*9 #index represents the digit value - 1
    while n:
        digit = n % 10 - 1
        if digits[digit] == 1:
            return False
        else:
            digits[digit] = 1
        n //= 10

    return True

for i in range(9876, 5123, -1): # only consider 4 digit numbers
    temp = i * 100000 + (i * 2)
    if is_pan(temp):
        print("Answer: ", temp)
        break
    
timing.endlog()
