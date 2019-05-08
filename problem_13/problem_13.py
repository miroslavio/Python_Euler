numbers= []
with open('large_number.txt','r', encoding='utf-16') as f:
    for line in f.readlines():
        numbers.append(int(line))

total_sum = str(sum(numbers))
print(total_sum[0:10])


