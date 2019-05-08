import math
import timing
import math

def not_both_odd(a, b):
    if a % 2 == 0 or b % 2 == 0:
        return True # at least one is even
    else:
        return False
    
def count_solutions(p):
    # Can apply Euclid's formula
    # a = m**2 - n**2
    # b = 2*m*n
    # c = m**2 + n**2
    # Use p = a + b + c to get:
    # p = 2*m*(m+n)
    count_ = 0
    m_lim = int(1 + 1/2 * math.sqrt(1/4 + p)) + 1
    repeat_vals = [] #all must be unique here
    for m in range(2, m_lim):
        for n in range(1, m):
            if math.gcd(m, n) == 1 and not_both_odd(m, n): # ensure all triplets are primitive!
                triplet = 2*m*(m+n)
                if p % triplet == 0:
                    count_ += 1
    return count_

max_solutions = 0
max_p = 0
for p in range(100, 1000):
    solutions = count_solutions(p)
    if solutions > max_solutions:
        max_solutions = solutions
        max_p = p
        
print("Solution count: ", max_solutions)
print("Answer: ", max_p)

timing.endlog()
