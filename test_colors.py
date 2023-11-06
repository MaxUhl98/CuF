import numpy as np
import matplotlib.pyplot as plt

n_0 = 19
iterations = 10**6
points = [n_0]
for i in range(iterations):
    if points[-1]%2 ==0:
        points.append(points[-1]/2)
    else:
        points.append(points[-1]*3 + 1)
plt.scatter(list(range(iterations+1)),points, s=1, color='blue')
plt.show()
