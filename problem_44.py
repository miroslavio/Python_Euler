import math

def is_pent( n ): 
    n = (1 + math.sqrt(24 * n + 1)) / 6
    return( (n - int (n)) == 0) 

flag = True
i = 1
diff = 0
while flag == True:
    i += 1
    p1 = int(i*(3*i-1)/2)
    for j in range(i - 1, 0, -1):
        p2 = int(j*(3*j-1)/2)
        if is_pent(p1 - p2):
            if is_pent(p1 + p2):
                diff = p1 - p2
                flag = False
                break
            
print("\nAnswer: ", diff)
                

            


    
