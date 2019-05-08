def check_digits(n): # return True only if n is 4 digits
    count_ = 0
    while n:
        n //= 10
        count_ += 1

    if count_ == 4:
        return True
    else:
        return False

def pandigital(a,b,c): # check if numbers a,b,c contain exclusively digits 1 to 9
    digits = []
    while c:
        i = c%10
        if i in digits or i == 0:
            return False
        else:
            digits.append(i)
            c //= 10
            
    while a:
        i = a%10
        if i in digits or i == 0:
            return False
        else:
            digits.append(i)
            a //= 10

    while b:
        i = b%10
        if i in digits or i == 0:
            return False
        else:
            digits.append(i)
            b //= 10
            
    return True

# a*b = c
# c must be a 4 digit number
# a and b can be 3 and 2 digit respectively
# a and b can also be 1 and 4 digit
products = []
for a in range(12, 99):
    for b in range(123, 988):
        c = a*b
        if check_digits(c):
            if pandigital(a,b,c):
                if c not in products:
                    print(a, b, c)
                    products.append(c)

for a in range(2, 10):
    for b in range(1234, 9877//2):
        c = a*b
        if check_digits(c):
            if pandigital(a,b,c):
                if c not in products:
                    print(a, b, c)
                    products.append(c)
                    
print("Answer: ", sum(products))
