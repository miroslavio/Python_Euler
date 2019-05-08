def magic(number):
    return int(''.join(str(i) for i in number))

def next_smaller(n):
    '''Permute digits in n such that it returns the next smaller permutation of its digits'''
    digits = [int(digit) for digit in str(n)]
    # start from the last digit to the first as long as the digits are decreasing or equal
    # i.e. if 987651234, then 5 is the first increase
    i = len(digits) - 1
    while i > 0 and digits[i - 1] <= digits[i]:
        i -= 1 # now i is the head of the increasing tail
    if i <= 0:
        return n # smallest permutation found

    # Find largest number in tail that is smaller than pivot=i-1
    j = len(digits) - 1
    while digits[j] >= digits[i - 1]:
        j -= 1
    # Swap pivot with largest number in tail
    digits[i - 1], digits[j] = digits[j], digits[i - 1]

    # Reverse tail
    digits[i : ] = digits[len(digits) - 1 : i - 1 : -1]

    # Reconstruct and return the number
    return magic(digits)

def next_larger(n):
    '''Permute digits in n such that it returns the next larger permutation of its digits'''
    digits = [int(digit) for digit in str(n)]
    # start from the last digit to the first as long as the digits are increasing or equal
    # i.e. if 12349876, then 4 is the first decrease
    i = len(digits) - 1
    while i > 0 and digits[i - 1] >= digits[i]:
        i -= 1 # now i is the head of the decreasing tail
    if i <= 0:
        return n # largest permutation found

    # Find number in tail that is larger than pivot=i-1
    j = len(digits) - 1
    while digits[j] <= digits[i - 1]:
        j -= 1
    # Swap pivot with largest number in tail
    digits[i - 1], digits[j] = digits[j], digits[i - 1]

    # Reverse tail
    digits[i : ] = digits[len(digits) - 1 : i - 1 : -1]

    # Reconstruct and return the number
    return magic(digits)
