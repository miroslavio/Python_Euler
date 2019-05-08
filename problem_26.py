# Find 1/d for d < 1000 that contains the longest recurring decimal cycle
# Use the principle of long division to quickly find the repeating cycles!
# And then calculate the size of the cycle
def cycle_count(d): # dividend is always 1, d will be divisor
    num = 1
    factor = 1
    while d > factor:
        factor *= 10
    num *= factor
    # Now can start the division process
    remainders = []
    count_ = 0
    while True:
        rem = num%d
        if rem == 0:
            count_ += 1
            break
        elif rem in remainders:
            break
        else:
            remainders.append(rem)
            num = rem*factor
            count_ +=1
            
    return count_

largest_cycle = 0
for d in range(2, 1000):
    if cycle_count(d) > largest_cycle:
        largest_cycle = d

print(largest_cycle)
