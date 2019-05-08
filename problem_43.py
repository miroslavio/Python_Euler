import permutations as perm

def check(n):
    '''Check if n fulfils the property given in the problem'''
    divisors = [17, 13, 11, 7, 5, 3, 2]
    for div in divisors:
        number = n % 1000
        if number % div != 0:
            return False
        n //= 10

    return True

num = 1023456789
sum_ = 0

while num < 9876543210:
    if check(num):
        print(num)
        sum_ += num
        
    num = perm.next_larger(num)
    
print("\nAnswer: ", sum_)
