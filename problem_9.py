# Find pythagorean triplet for which a+b+c = 1000 and give their product
from math import sqrt

# This will form the core of the solution since we know for certain that all
# a, b and c must be square numbers 
def is_square(n):
    return sqrt(n).is_integer()

# Can also exploit the fact that we must have that for two integers a and b,
# their sum must give a square number.
# Or use algebra:
# a + b + sqrt(a**2+b**2) == 1000
def condition(a, b):
    c = sqrt(a**2 + b**2)
    if c.is_integer():
        c = int(c)
    if a + b + c == 1000:
        return True
    else:
        return False

for a in range(1, 1000):
    for b in range(a, 1000):
        if condition(a, b):
            print(a*b*(1000-a-b))
        

