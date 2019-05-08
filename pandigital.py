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
