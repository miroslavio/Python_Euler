import sieve
primes = sieve.sieve(10000000) # try up to this limit
##def repeat_dig(n):
##    digits = [0]*10
##    while n:
##        digit = n%10
##        if digits[digit] == 1: # repeat digit found
##            return True
##        else:
##            digits[n%10] = 1
##        n //= 10
##        
##    return False
def repeat_dig(n):
    digits = [0]*10
    while n:
        digits[n%10] += 1 
        
    return digits # any value in this list greater than one indicates a repeated digit

def replace_dig(n): # minimum of two digits must be replaced up to but not including the last digit
    digits = repeat_dig(n)
    for i in range(len(digits)):
        if digits[i] > 1: # repeat digit found
    

for i in range(100000, len(primes)):
    if primes[i] == 1 and repeat_dig(i):
        
