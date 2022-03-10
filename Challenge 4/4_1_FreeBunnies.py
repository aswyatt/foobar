from itertools import combinations

def solution(Nb, Nr):
    if Nr==1:
        return [[0] for nb in range(Nb)]
    elif Nr==Nb:
        return [[nb] for nb in range(Nb)]
    keys = [[] for nb in range(Nb)]
    ind = [n for n in range(Nr)]
    key = 0
    while True:
        for ni in range(Nr):
            keys[ind[ni]].append(key)
        key += 1
        # print(ind)
        ni = Nr-1
        while ind[ni]==Nb-(Nr-ni):
            ni -= 1
        if ni<0:
            break
        ind[ni] += 1
        if ni<Nr-1:
            for n in range(ni+1, Nr):
                ind[n] = ind[n-1]+1
    return keys




def solution1(num_buns, num_required):
    # Initialize the list of keys
    keyrings = [[] for num in range(num_buns)]
    # Calculate how many copies are required
    # per each key
    copies_per_key = num_buns - num_required + 1
    # Append keys in the list initialized above
    for key, bunnies in enumerate(combinations(range(num_buns), copies_per_key)):
        for bunny in bunnies:
            keyrings[bunny].append(key)

    return keyrings

# import numpy as np
# def solution(Nb, Nr):
#     N = 1+Nb-Nr
#     #   Number of permutations
#     #       sum(n*(N+1-n) for n=1:N) or
#     #       sum((n+1)*(N-n) for n=0:N-1)
#     Np = (N*(N+1)*(N+2))//6
#     #   Number of columns in result: sum(n, n=1:N) or sum(n+1, n=0:N-1)
#     COLS = (N*(N+1))//2
#     #   Result list of lists
#     res = [[0]*Nb for i in range(COLS)]
#     #   List of column indices (initially 0)
#     cols = [0]*Nb
#     #   List of row indices (initially 0:R-1)
#     rows = range(Nr)

#     for n0 in range(N):



#     # #   Loop through each permutation
#     # for np in range(Np):
#     #     #   Loop through each console
#     #     for r in rows:
#     #         res[r][cols[r]] = np
#     #         cols[r] +=1


# # def UpdateRows(rows):
#     # rows


# def solution(num_buns, num_required):
#     if num_required==1:
#         return [[0] for n in range(num_buns)]

#     result = [[] for n in range(num_buns)]
#     ind = [n for n in range(num_required)]
#     iter = 0
#     while ind[0]<num_buns-num_required+1:
#         for ind[-1] in range(ind[-2]+1, num_buns):
#             for nr in range(num_required):
#                 result[ind[nr]].append(iter)
#             iter += 1
#         indr = num_required-2
#         while indr and (ind[indr]==num_buns-(num_required-indr)):
#             indr -= 1
#         ind[indr] += 1
#         for nr in range(indr+1, num_required):
#             ind[nr] = ind[nr-1]+1
#     return result

# print(solution(2,1))
# print(solution(4,4))
# print(solution(5,3))
# print(solution(4,2))
# print(solution(6, 3))
print(solution(8,4))
print(solution1(8,4))