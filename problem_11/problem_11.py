
# Find greatest product of 4 adjacent numbers in the same direction

# Create a 2D array called grid to store all numbers as strings for now.
grid = []
with open('grid.txt','r', encoding='utf-16') as f:
    for line in f:
        grid.append(line.split())

# Use int() to treat them as numbers, int('08')=8 <-- useful

top_product = 0
nrows = len(grid)
ncols = len(grid[0])
product = 1

# HORIZONTAL
for i in range(0, nrows):
    for j in range(0, ncols-3):
        for k in range(j, j+4):
            product *= int(grid[i][k])
        if product > top_product:
            top_product = product
        product = 1

# VERTICAL
for i in range(0, ncols):
    for j in range(0, nrows-3):
        for k in range(j, j+4):
            product *= int(grid[k][i])
        if product > top_product:
            top_product = product
        product = 1

# DIAGONAL \\\
for j in range(0, nrows-3):
    for k in range(0, ncols-3):
        for i in range(0, 4):
            product *= int(grid[i+j][i+k])
        if product > top_product:
            top_product = product
        product = 1
    
# DIAGONAL ///
for j in range(0, nrows-3):
    for k in range(ncols-1, 2, -1):
        for i in range(0, 4):
            product *= int(grid[i+j][k-i])
        if product > top_product:
            top_product = product
        product = 1

# RETURN ANSWER
print(top_product)
        
