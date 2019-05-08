names = []

with open('names.txt', 'r') as f:
    contents = f.read()
    for entry in contents.split(','):
        names.append(entry.strip('\"'))
    
# Sort alphabetically
names.sort()

def string_val(s):
    return sum([ord(c)-64 for c in s]) # list comprehension
    
answer = 0

for i in range(len(names)):
    answer += string_val(names[i])*(i+1)

print(answer)
    
