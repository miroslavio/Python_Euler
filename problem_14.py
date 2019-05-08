def collatz(n): # give next term in the collatz sequence
    if n%2 == 0:
        return int(n/2)
    else:
        return int(3*n + 1)


limit = 1000000
longest_chain = 1
longest_chain_num = 1
number = 1

while number <= limit:
    start = number
    counter = 0
    while start > 1:
        start = collatz(start)
        counter += 1
    if counter > longest_chain:
        longest_chain = counter
        longest_chain_num = number
    number += 1

print("\nChain length: ", longest_chain)
print("\nStarting number: ", longest_chain_num)
    
