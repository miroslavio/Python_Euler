dict = {1:1}

print("\nBefore: ", dict)

def expand():
    dict[13] = 10

expand()
print("After: ", dict)

def check():
    if 13 in dict:
        print(True)

check()
