def is_palindrome(n, base = 10):
    rev = 0
    k = n
    while k:
        rev = base*rev + k % base
        k //= base
    return n == rev
    
def lych(n, base = 10):
    rev = 0
    k = n
    while k:
        rev = base*rev + k % base
        k //= base
    return n + rev

count = 0
for i in range(10000):
    num = i
    is_lychrel = True
    for j in range(50):
        num = lych(num)
        if is_palindrome(num):
            is_lychrel = False
            break # not a lychrel number
    if is_lychrel == True:
        count += 1


print("\nAnswer: ", count)
