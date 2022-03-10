from itertools import combinations

def solution(num_bun, num_required):
    if num_required<1:
        return [[] for nb in range(num_bun)]
    elif num_required==1:
        return [[0] for nb in range(num_bun)]
    elif num_required==num_bun:
        return [[nb] for nb in range(num_bun)]
    keys = [[] for nb in range(num_bun)]
    bunnies = [n for n in range(num_required)]
    key = 0
    comb = []
    while True:
        for bunny in bunnies:
            keys[bunny].append(key)
        comb.append(bunnies)
        key += 1
        nb = num_required-1
        while bunnies[nb]==num_bun-(num_required-nb):
            nb -= 1
        if nb<0:
            break
        bunnies[nb] += 1
        if nb<num_required-1:
            for n in range(nb+1, num_required):
                bunnies[n] = bunnies[n-1]+1
    return comb

def solution1(num_buns, num_required):
    # Initialize the list of keys
    keys = [[] for num in range(num_buns)]
    # Number of key copies
    num_copy = num_buns - num_required + 1
    #   Generate combinations
    bunny_comb = combinations(range(num_buns), num_copy)
    comb = []
    for key, bunnies in enumerate(bunny_comb):
        comb.append(bunnies)
    return comb
    # Loop through combinations, adding key to list
    for key, bunnies in enumerate(bunny_comb):
        for bunny in bunnies:
            keys[bunny].append(key)
    #   Return result
    return keys

for nb in range(3, 5):
    for nr in range(2, nb):
        print(solution(nb,nr))
        print(solution1(nb,nr))
        print("\n")