import timing
import permutations

def is_prime(n): 
    if n < 2:
        return False
    
    i = 2
    # Loop from 2 to int(sqrt(n))
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


n = 7654321 # Start from first potential candidate as 8 and 9 digits are always divisible by 3
while n > 1234567: # assuming answer is a 9-digit number
    if is_prime(n):
        print("\nAnswer: ", n)
        break
    else:
        n = permutations.next_smaller(n) # permutate n to smaller iteration

timing.endlog()
