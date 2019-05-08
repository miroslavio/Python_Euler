def is_palindrome(n, base):
    reversed = 0
    k = n
    while k:
        reversed = base*reversed + k % base
        k //= base
    return n == reversed

limit = int(1e6)
sum_ = 0
for i in range(1, limit, 2): # number must be odd to be palindromic in base 2
    if is_palindrome(i, 10) and is_palindrome(i, 2):
        sum_ += i

print("Answer: ", sum_)
