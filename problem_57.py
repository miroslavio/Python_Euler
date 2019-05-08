def next_iter(frac):
    return [frac[0] + 2*frac[1], frac[0] + frac[1]]

def num_more(frac):
    count_num = 0
    count_den = 0
    num = frac[0]
    den = frac[1]
    while num:
        count_num += 1
        num //= 10
    while den:
        count_den += 1
        den //= 10
    return count_num > count_den

# List represents the fraction
fraction = [3, 2]

answer = 0
for i in range(1000):
    if num_more(fraction):
        answer += 1
    fraction = next_iter(fraction)

print("\nAnswer: ", answer)
