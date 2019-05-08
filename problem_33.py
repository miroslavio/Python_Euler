from fractions import Fraction

def non_trivial(n, d): 
    """Return True if it is a digit cancelling fraction
    n = numerator, d = denominator"""
    original = n/d
    #print("Original fraction value: ", original)
    n_digits = []
    d_digits = []
    while n:
        n_digits.append(n%10)
        n //= 10
    while d:
        d_digits.append(d%10)
        d //= 10
    #print("Numerator digits: ", n_digits)
    #print("Denominator digits: ", d_digits)
    # check for common digits
    common_digits = list(set(n_digits) & set(d_digits))
    if common_digits:
        n_digits.remove(common_digits[0])
        d_digits.remove(common_digits[0])
        if n_digits[0]/d_digits[0] == original:
            return True
    
    return False
                

nt_fractions = []
for num in range(11, 99):
    if num % 10 == 0 or num% 11 == 0:
        continue
    for den in range(num+1, 100):
        if den % 10 == 0 or den % 11 == 0:
            continue
        if non_trivial(num, den):
            nt_fractions.append(Fraction(num, den))
            print(num, "/", den)
            
answer = Fraction(1, 1)
for fraction in nt_fractions:
    answer *= fraction

print("\nAnswer: ", answer)


