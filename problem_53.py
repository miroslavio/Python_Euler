import math as m

def nCr(n, r):
    return m.factorial(n) / (m.factorial(r) * m.factorial(n - r))

count = 0
for n in range(20, 101):
    for r in range(1, n + 1):
        if nCr(n, r) > 1000000:
            count += 1

print("\nAnswer: ", count)
