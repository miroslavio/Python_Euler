def same_digits(a, b):
    digits_a = [0]*10
    digits_b = [0]*10
    while a:
        digits_a[a%10] += 1
        a //= 10
    while b:
        digits_b[b%10] += 1
        b //= 10

    return digits_a == digits_b

answer = 0
i = 100 
while answer == 0:
    count = 0
    for j in range(2, 7):
        if same_digits(i, i*j) == False:
            break
        else:
            count += 1
    if count == 5:
        answer = i
    i += 1

print("\nAnswer: ", answer)
