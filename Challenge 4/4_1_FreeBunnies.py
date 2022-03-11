from itertools import combinations
from time import perf_counter_ns as pc

def solution(num_bun, num_required):
    #   Return trivial cases
    if num_required<1:
        #   No bunnies required!
        return ([[] for nb in range(num_bun)], [])
    if num_required==1:
        #   All bunnies have the same key (0)
        return ([[0] for nb in range(num_bun)], [[nb for nb in range(num_bun)]])
    if num_required==num_bun:
        #   All bunnies have a unique key (0:num_bun-1)
        return ([[nb] for nb in range(num_bun)], [[nb] for nb in range(num_bun)])

    #   Since any num_required-1 bunnies is insufficient, the remaining bunnies must have the same additional key, hence we need to find the number of combinations for num_bun with num_bun-(num_required-1)
    combos = GetCombos(num_bun, num_bun-num_required+1)

    #   Given all the combinations, find the key distribution for num_bun
    keys = GetKeys(combos, num_bun)
    return (keys, combos)

def GetKeys(combos, Nb):
    #   Initialise keys list
    keys = [[] for b in range(Nb)]
    #   First key = 0
    key = 0
    #   Loop through all combinations
    for combo in combos:
        #   Give current key to bunnies listed in current combo
        for bunny in combo:
            keys[bunny].append(key)
        #   Increment key
        key += 1
    return keys

def GetCombos(Nb, Nr):
    #   Need to find combination of bunnies without a key:
    #   e.g. for (6, 4)
    #   bunny ----------->
    #            0 1 2 3 4 5
    #   combo  0 x x x x
    #      |   1 x x x   x
    #      |   2 x x x     x
    #      |   3 x x   x x
    #      V   4 x x   x   x
    #   etc.
    bunnies = [nb for nb in range(Nr)]
    combos = []
    while True:
        # for nb in range(Nr):
        #     keys[bunnies[nb]].append(key)
        combos.append([b for b in bunnies])
        # key += 1
        nb = Nr-1
        while bunnies[nb]==Nb-(Nr-nb):
            nb -= 1
        if nb<0:
            break
        bunnies[nb] += 1
        if nb<Nr-1:
            for n in range(nb+1, Nr):
                bunnies[n] = bunnies[n-1]+1
    return combos

def solution1(num_buns, num_required):
    # Initialize the list of keys
    keys = [[] for num in range(num_buns)]
    # Number of key copies
    num_copy = num_buns - num_required + 1
    #   Generate combinations
    bunny_comb = combinations(range(num_buns), num_copy)

    comb = []
    # Loop through combinations, adding key to list
    for key, bunnies in enumerate(bunny_comb):
        comb.append([b for b in bunnies])
        for bunny in bunnies:
            keys[bunny].append(key)
    #   Return result
    return (keys, comb)

for nb in range(1, 10):
    for nr in range(0, nb+1):
        pc0 = pc()
        k0, c0 = solution(nb,nr)
        pc1 = pc()
        k1, c1 = solution1(nb,nr)
        pc2 = pc()
        print("("+str(nb)+", "+str(nr)+"):")
        print(" c:", c0)
        print("c1:", c1)
        print(" k:", k0)
        print("k1:", k1)
        print("Elapsed time   [us]:", int(1e-3*(pc1-pc0)))
        print("Elapsed time 1 [us]:", int(1e-3*(pc2-pc1)))
        print("\n")

# nb = 9
# nr = 7
# pc0 = pc()
# k0, c0 = solution(nb,nr)
# pc1 = pc()
# k1, c1 = solution1(nb,nr)
# pc2 = pc()
# print("("+str(nb)+", "+str(nr)+"):")
# print(" c:", c0)
# print("c1:", c1)
# print(" k:", k0)
# print("k1:", k1)
# print(" Elapsed time  [us]:", int(1e-3*(pc1-pc0)))
# print("Elapsed time 1 [us]:", int(1e-3*(pc2-pc1)))
# print("\n")