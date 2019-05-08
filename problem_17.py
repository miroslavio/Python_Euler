def letterCount(num):
    numbers = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", \
               6:"six", 7:"seven", 8:"eight", 9:"nine", \
               10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", \
               15:"fifteen", 18:"eighteen", 20:"twenty", \
               30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", \
               70:"seventy", 80:"eighty", \
               90:"ninety", 1000:"onethousand"}
    
    # Now have all unique words up to one thousand except hundred
    if num in numbers:
        return len(numbers[num]) # When faced with a unique number

    # TEENS DONE
    elif num < 20:
        return len(numbers[num%10]) + 4 # 4 is for "teen"

    # 20 to 99
    elif num < 100:
        part_one = num - (num%10) #43 turns to 40, etc
        return len(numbers[part_one] + numbers[num%10])

    # 100 to 999
    elif num < 1000: # These numbers sometimes contain AND
        first_digit = num//100
        if num % 100 == 0: # NO AND for this occurence
            return len(numbers[first_digit]) + 7 # 7 for hundred
        else: # Add 10 since AND must be included
            return len(numbers[first_digit]) + letterCount(num%100) + 10
        
    else: #Numbers outside required range
        return 0
    
letter_count = 0
end_point = 1000

for i in range(1, end_point+1): #+1 so it is inclusive of last number
    print("Number: ", i, ", Letter count: ", letterCount(i))
    letter_count += letterCount(i)

print(letter_count)



