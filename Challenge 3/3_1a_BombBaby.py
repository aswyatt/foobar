import numpy as np

def solution(M,F):
    M = eval(M.replace("^", "**"))
    F = eval(F.replace("^", "**"))

    #   Check trivial cases
    if (M==1):
        return str(F-1)
    elif (F==1):
        return str(M-1)

    #   Check non-trivial cases
    tree = BombTree(M, F)
    while (tree.status is None):
        tree.increment()
        print(tree.gen, tree.data.size)

    #   Return number of generations or impossible
    return tree.status

#   Due to symmetry, we can swap M & F so only need to do half the calcs
#   Start at [1,2] since [1,1] is trivial
class BombTree:
    def __init__(self, M, F):
        self.max = np.array([[M], [F]])
        self.gen = 1
        self.data = np.array([[1], [2]])
        self.status = None

    def increment(self):
        a = self.data
        #   Increment generation number
        self.gen += 1
        #   Add M & F
        s = a.sum(axis=0)
        #   Generate new array
        self.data = np.vstack((a.flatten(), np.tile(s, 2)))
        #   Update status
        self.removeInvalid()
        self.check()

    def removeInvalid(self):
        a = self.data
        #   Check for # > (M,F)
        ind = (np.all(a<=self.max, axis=0)
               | np.all(a<=np.flipud(self.max), axis=0))
        #   Keep valid values
        self.data = a[:, ind]

    def check(self):
        a = self.data
        if not a.size:
            self.status = "impossible"
        elif not self.check_(False):
            self.check_(True)

    def check_(self, flip=False):
        a = self.data
        if flip:
            b = self.max
        else:
            b = np.flipud(self.max)
        iseq = (a==b)
            # (np.any(np.all(a==self.max, axis=0))
            #     | np.any(np.all(a==np.flipud(self.max), axis=0))):
            # self.status = str(self.gen)
        return False

# print(solution('4', '7'))
# print(solution('2', '1'))
# print(solution("2", "4"))
print(solution("10^10", "50"))