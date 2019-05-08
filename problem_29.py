terms = []

lim = 100
for a in range(2, lim+1):
    for b in range(2, lim+1):
            if a**b not in terms:
                terms.append(a**b)

print(len(terms))
