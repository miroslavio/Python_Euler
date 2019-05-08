dig_count = 0
counter = 1
answer = 1
for i in range(1, 1000000):
    temp = i
    digits = [] # store digits of number here
    while temp:
        digits.append(temp % 10)
        temp //= 10
    j = len(digits) - 1
    while j >= 0:
        dig_count += 1 #count every single digit
        if dig_count == counter:
            counter *= 10
            answer *= digits[j]
            print("Digit count: ", dig_count, "Digit: ", digits[j])
        j -= 1

print("\nAnswer: ", answer)
            
        
            
