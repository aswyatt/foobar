import numpy as np

#   Rather than calculating laser beam reflections, we simply replicate ourself/trainer via reflections about each wall, and then repeat up to the maximum distance travelled by the laser. This can be done in "1 step" by generating an array of replication indices
def solution(dimensions, your_position, trainer_position, distance):
    #   Extract parameters to make life easier
    (width, height) = dimensions
    (x0,y0) = your_position
    (x1,y1) = trainer_position

    #   Generate index arrays
    #   This could be done a little more efficiently, but this is readable
    nx_max = 1 + np.floor((distance+x0)/(2*width))
    ny_max = 1 + np.floor((distance+y0)/(2*width))
    nx = np.arange(-nx_max, nx_max+1)
    ny = np.arange(-ny_max, ny_max+1)

    sgn = np.array([1, -1]).reshape((-1,1))

    #   Replicated my positions
    X0 = (2*nx*width + sgn*x0).flatten()
    Y0 = (2*ny*height + sgn*y0).flatten()

    #   Replicated trainer positions
    X1 = (2*nx*width + sgn*x1).flatten()
    Y1 = (2*ny*height + sgn*y1).flatten()

    #   Only keep those within square of size 2*dist
    indx = (abs(X0-x0)<=distance) & (abs(X1-x0)<=distance)
    indy = (abs(Y0-y0)<=distance) & (abs(Y1-y0)<=distance)

    #   Generate meshgrid
    (X0, Y0) = np.meshgrid(X0[indx], Y0[indy])
    (X1, Y1) = np.meshgrid(X1[indx], Y1[indy])
    X0 = X0.flatten()
    Y0 = Y0.flatten()
    X1 = X1.flatten()
    Y1 = Y1.flatten()

    #   Calculate square distances
    dX0 = X0-x0
    dY0 = Y0-x0
    dX1 = X1-x0
    dY1 = Y1-x0
    d20 = dX0**2 + dY0**2
    d21 = dX1**2 + dY1**2

    #   Calculate tan(theta) = y/x
    th0 = dY0/dX0
    th1 = dY1/dX1

    #   Get indices where:
    #       tan(theta0)=y0/x0 == tan(theta1)=y1/x1 --> x0*y1 != x1*y0
    #       and d21<d20
    ind = np.any(
        ((th0.reshape((-1,1)))==th1)
        & ((d20.reshape((-1,1)))<=d21), axis=0)

    #   Return sum of those with dist<max_dist
    ind = np.bitwise_not(ind) & (d21<=(distance**2))
    count = len(np.unique(th1[ind]))
    return count

dim = [3,2]
pos0 = [1,1]
pos1 = [2,1]
max_dist = 4

# dim = [300, 275]
# pos0 = [150, 150]
# pos1 = [185, 100]
# max_dist = 500

print(solution(dim, pos0, pos1, max_dist))
