import numpy as np
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


def solution(Nb, Nr):
    if Nr==1:
        return [[0] for n in range(Nb)]

    res = [[] for n in range(Nb)]
    ind = [n for n in range(Nr)]
    iter = 0
    while ind[0]<Nb-Nr+1:
        for ind[-1] in range(ind[-2]+1, Nb):
            for nr in range(Nr):
                res[ind[nr]].append(iter)
            iter += 1
        indr = Nr-2
        while indr and (ind[indr]==Nb-(Nr-indr)):
            indr -= 1
        ind[indr] += 1
        for nr in range(indr+1, Nr):
            ind[nr] = ind[nr-1]+1
    return res

# print(solution(2,1))
print(solution(4,4))
# print(solution(5,3))
