import numpy as np
import matplotlib.pyplot as plt

def affine(point, *args):

    p_new = point @ args[0]
    return p_new + args[1]
transform = (np.array([[.99999, 0], [0, .99999]]), np.array([0.000008, 0.000008]))

triang = [np.array([1,1]),np.array([2,1]),np.array([1,2]),np.array([1,1])]
points = [*triang]
iterations = 10000
for i in range(iterations):
    n_triang = [affine(points[-1], *transform),affine(points[-2], *transform),affine(points[-3], *transform),affine(points[-1], *transform) ]
    points += n_triang
x, y = [i[0] for i in points], [i[1] for i in points]
# Scatterplot erstellen und anzeigen
plt.plot(x, y, color='blue')
# plt.plot(x,y)
plt.axis('equal')
plt.show()