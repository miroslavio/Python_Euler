# From coin obtain the next list of largest coins that can make up coin
def split_coin(coin):
    if coin == 200:
        return [100, 100]
    if coin == 100:
        return [50, 50]
    if coin == 50:
        return [10, 20, 20]
    if coin == 20:
        return [10, 10]
    if coin == 10:
        return [5, 5]
    if coin == 5:
        return [1, 2, 2]
    if coin == 2:
        return [1, 1]
    if coin == 1:
        return [1]


target = 200
ways = 0

for a in range(target, -1, -200):
    for b in range(a, -1, -100):
        for c in range(b, -1, -50):
            for d in range(c, -1, -20):
                for e in range(d, -1, -10):
                    for f in range(e, -1, -5):
                        for g in range(f, -1, -2):
                            ways += 1
print(ways)
        
