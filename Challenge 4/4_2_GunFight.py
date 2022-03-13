import numpy as np

#   Generates linear array [N x 2] = [x, y] of reflected positions
def GetPositions(nmax, dim, pos, pos0, max_dist):
    #   Generate array of positions
    a = np.array([-1, 1]).reshape((-1,1))
    x = 2*np.arange(-nmax[0], nmax[0]+1)*dim[0] + a*pos[0]
    y = 2*np.arange(-nmax[1], nmax[1]+1)*dim[1] + a*pos[1]

    #   Select those within range
    x = x[abs(x-pos0[0])<=max_dist]
    y = y[abs(y-pos0[1])<=max_dist]

    #   Generate mesh grid
    (x,y) = np.meshgrid(x, y)
    return np.vstack((x.flatten(), y.flatten()))

#   Calculates distance vectors and returns those less than distance
def GetDistances(POS, pos0, max_dist):
    #   Array if distance vectors
    delta = POS-np.array(pos0).reshape((-1,1))

    #   Squared distances
    d2 = np.sum(delta**2, axis=0)

    #   Inices where distance within range and not zero
    ind = (d2<=max_dist**2) & (d2>0)

    #   Select data subset
    return (delta[:, ind], d2[ind])

#   Find where tan(theta1) == tan(theta2)
#   Could calculate atan2(y, x), but this will convert to floating point and thus requires a tolerance setting (which could be calculated based on dim)
#   Instead I use tan(theta)=y/x ==> find (y1*x2==x1*y2) and check the quadrant of theta (i.e. relative signs of y1,y2 and x1,x2)
def TanMatrix(delta1, delta2):
    x1 = delta1[0,:]
    y1 = delta1[1,:]
    x2 = delta2[0,:].reshape((-1,1))
    y2 = delta2[1,:].reshape((-1,1))
    return (np.arctan2(y1, x1)==np.arctan2(y2,x2))
    # return ((y1*x2==x1*y2)
    #         & (np.sign(y1)==np.sign(y2))
    #         & (np.sign(x1)==np.sign(x2)))

#   Rather than calculating laser beam reflections, we simply replicate ourself/trainer via reflections about each wall, and then repeat up to the maximum distance travelled by the laser. This can be done in "1 step" by generating an array of replication indices
def solution(dimensions, your_position, trainer_position, distance):
    #   Get maximum reflection index
    nmax = np.floor(0.5*(distance + 2*np.array(your_position))/np.array(dimensions)).astype(int)
    #   Generate arrays of reflected positions for myself and trainer
    POS0 = GetPositions(nmax, dimensions, your_position, your_position, distance)
    POS1 = GetPositions(nmax, dimensions, trainer_position, your_position, distance)
    #   Get distances of reflected points from your positions
    (delta0, d20) = GetDistances(POS0, your_position, distance)
    (delta1, d21) = GetDistances(POS1, your_position, distance)
    #   Generate indices of points where !((tan(theta0)==tan(theta2) & dist0<=dist1)
    ind = np.logical_not(np.any(TanMatrix(delta0, delta1) & (d20<=d21.reshape((-1,1))), axis=1))
    delta1 = delta1[:, ind]
    #   Get unique directions & return size
    n = np.arange(delta1.shape[1])
    ind = np.any(TanMatrix(delta1, delta1) & (n>n.reshape((-1,1))), axis=1)
    # return int(np.sum(1-ind))
    return len(ind[np.logical_not(ind)])

TEST = 1
if TEST==1:
    dimensions = [3,2]
    your_position = [1,1]
    trainer_position = [2,1]
    distance = 4
elif TEST==2:
    dimensions = [300, 275]
    your_position = [150, 150]
    trainer_position = [185, 100]
    distance = 500
elif TEST==3:
    dimensions = [5,7]
    your_position = [2,3]
    trainer_position = [4,1]
    distance = 15


print(solution(dimensions, your_position, trainer_position, distance))
