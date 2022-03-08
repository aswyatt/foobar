import numpy as np

# l = np.array([2, 3, 4, 6, 8, 9, 10, 12])
l = np.arange(1, 7)
N = len(l)

r = l[1:].reshape((1,-1))
c = l[:-1].reshape((-1,1))
d = (r%c)==0

v = np.arange(len(l)-1).reshape((1,-1))
m = v.transpose()<=v

M = np.logical_and(d, m)
# M1 =M[:, :-1].reshape((N-1,N-2,1))
# M2 = M[1:, :]
M1 = M[:, :-1]
M2 = M[1:, :]
count = 0
for n in range(N-2):
    count += np.sum(M2[M1[n, :], :])

print(np.sum(M1 & M2))