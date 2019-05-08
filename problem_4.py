# Find largest palindromic number made from product of two 3-digit numbers

# Core function to this problem, must be efficient
def is_palindrome(x):
    str1 = str(x)
    str2 = str1[::-1] # Syntax to reverse a string
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

# Double for loop could go through all potential combinations two
# 3-digit products, but there must be a shortcut.
# You can half number of calculations by eliminating repeated combinations of
# multiples by simply enforcing i < j.
# Another shortcut as suggested by euler is to simply count backwards
# to speed up the search for the largest palindrome.

largest_n = 0
for i in range(999,99,-1):
    for j in range(999,i,-1):
        n = i*j
        if n < largest_n:
            break # Since i*j is always going to be too small
        if is_palindrome(n):
            largest_n = n


print(largest_n)
