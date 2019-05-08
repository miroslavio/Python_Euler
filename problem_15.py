grid_size = 1000 #more intuitive if count lattice points

grid = [1] * grid_size

for j in range(grid_size-1):
    for i in range(1, grid_size):
        grid[i] = grid[i-1] + grid[i]


print(grid[-1])
