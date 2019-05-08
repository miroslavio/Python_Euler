def word_val(word):
    val = 0
    for i in word:
        val += ord(i) - 64
    return val

triangles = [int(0.5*n*(n+1)) for n in range(1, 25)]
words = []

with open('words.txt', 'r') as f:
    contents = f.read().split(',')
    for entry in contents:
        words.append(entry.strip('\"'))

count = 0
for word in words:
    if word_val(word) in triangles:
        count += 1

print("\nAnswer: ", count)
