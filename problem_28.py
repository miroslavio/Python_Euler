# Take a list of numbers and treat it as a spiral summing only numbers found in diagonals
def sum_diags(spiral):
    sum_ = 1 # start from the middle of the spiral
    size_step = 2 # at every border the step between diagonal numbers increases by 2
    count_ = 0 # count to 4, indicate step to new border
    i = 2 # start from first diagonal number
    while i <= len(spiral):
        sum_ += spiral[i] 
        count_ += 1 
        if count_ == 4:
            size_step += 2 
            count_ = 0 # reset counter
        i += size_step
        

    return sum_

# Last number of the spiral indicates the size, i.e. for 3x3 the last number is 3*3 = 9
# Therefore for a 1001x1001 spiral, last number must be 1001*1001
spiral_size = 1001
assert spiral_size%2 != 0, "SPIRAL SIZE CANNOT BE EVEN!"
numbers = list(range(1, spiral_size*spiral_size+1))

print(sum_diags(numbers))
