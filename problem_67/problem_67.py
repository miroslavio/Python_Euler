# Get the triangle into a readible format into your code
triangle = []

# Read in the file
with open('triangle.txt', 'r') as f:
    for line in f:
        triangle.append(line.split())

# Convert all numbers to integers
nrows = len(triangle)
for i in range(nrows):
    for j in range(len(triangle[i])):
        triangle[i][j] = int(triangle[i][j])

print(triangle)
# Solution
# Go row by row adding adjacent numbers and retaining the largest sums
# It is easier to backwards and reduce the rows
# There are always two sums and you must pick the largest one
# triangle[i][j] = max(triangle[i+1][j]+triangle[i][j], triangle[i+1][j+1]+triangle[i][j])
# del(triangle[i+1])

for i in range(len(triangle)-1, 0, -1):
    for j in range(len(triangle[i-1])):
        triangle[i-1][j] = max(triangle[i-1][j]+triangle[i][j], \
                               triangle[i-1][j]+triangle[i][j+1])

    
print(triangle[0][0])
