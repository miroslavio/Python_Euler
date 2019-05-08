def fibonacci(n): #Recursion is very slow, do not use this
    if n<2:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

# Starting numbers and limit
limit = 4e6 #4 million
num_1 = 1
num_2 = 2
total_sum = 0 # Final answer

while num_2 < limit:
    if num_2%2 == 0: # Check if even
        total_sum += num_2
        
    # Perform a step in Fibonacci sequence
    temp = num_1+num_2
    num_1 = num_2
    num_2 = temp

print(total_sum)
    
