values = {1:1} # Great efficiency by storing Collatz(n) = a

def countChain(n): # Recursive function
    if n in values:
        return values[n] # return already computed chain length
    
    if n%2==0:
        values[n] = 1 + countChain(n/2) # key = number, value = chain length
    else:
        values[n] = 2 + countChain((3*n + 1)/2) # save a step with this

    return values[n]

longest_chain = 0
answer = -1

start = int(5e5)
limit = int(1e6)
for number in range(start+1, limit,2):
    chain_length = countChain(number)
    if chain_length > longest_chain:
        longest_chain = chain_length
        answer = number

print(answer)
        
