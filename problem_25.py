# Do not have to count digits for every term in the sequence.
# store each two terms in the sequence and if their sum exceeds a factor of 10, then increment
# number of digits by 1
digit_lim = 1000
digit_number = 1
a = 1
b = 1
index = 2 # start from second term F_2

while digit_number < digit_lim:
    temp = a + b
    a = b
    b = temp
    index += 1
    if b > 10**digit_number:
        digit_number += 1

print(index)


