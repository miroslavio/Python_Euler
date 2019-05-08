from math import sqrt

def primeFactors(n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2,)
        n = n/2

    # n must be odd at this point
    for i in range(3, int(sqrt(n))+1, 2): #increment in steps of 2 so odd division is applied
        while n % i == 0:
            print(i,)
            n = n / i

number = 600851475143
primeFactors(number)
                   
                   
                   
                   
