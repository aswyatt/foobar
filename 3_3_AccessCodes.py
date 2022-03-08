import numpy as np
import time
import random

def solution(l):
    #   Check trivial case
    if len(l)<3:
        return 0
    #   Convert to numpy array & count
    return Count(np.array(l))

def Count(l):
    #   Length used later
    N = len(l)

    #   Calculate divisibility matrix:
    #       d_nm = True if ln divides lm
    r = l[1:].reshape((1,-1))
    c = l[:-1].reshape((-1,1))
    d = (r%c)==0

    #   since we want i < j < m, need to consider upper triangular matrix only
    v = np.arange(len(l)-1).reshape((1,-1))
    m = v.transpose()<=v
    M = np.logical_and(d, m)

    #   Find y divides z where x divides y
    M1 = M[:, :-1]
    M2 = M[1:, :]
    count = 0
    for n in range(N-2):
        count += np.sum(M2[M1[n,:], :])

    #   Return result
    return count

# def Count(l):
#     count = 0
#     for n0 in range(l.size):
#         l1 = isDivisible(l[n0], l[n0+1:])
#         for n1 in range(l1.size):
#             count += isDivisible(l1[n1], l1[n1+1:]).size
#     return count

# def Count(l):
#     count = 0
#     for n0 in range(len(l)):
#         l0 = l[n0]
#         l1 = l[n0+1:]
#         l1 = [L for L in l1 if not L%l0]
#         for n1 in range(len(l1)):
#             l0 = l1[n1]
#             l2 = l1[n1+1:]
#             count += len([L for L in l2 if not L%l0])
#     return count


print(solution(range(1,7)))
print(solution([1,1,1]))
print(solution([3, 5, 1, 7, 11, 1, 13, 1, 17]))
MAX = 10
N = 2000
T = 0
for n in range(10):
    l = [random.randint(1, MAX) for n in range(N)]
    T1 = time.clock()
    s = solution(l)
    T2 = time.clock()
    T+= (T2-T1)
    print("Elapsed time: " + str(T))
# print("s: "+str(s))
