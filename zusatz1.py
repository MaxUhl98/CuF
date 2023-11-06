import numpy as np
import matplotlib.pyplot as plt
import random


def affine(point, *args):
    p_new = point @ args[0]
    return p_new + args[1]


transforms = [
    (np.array([[.8, 0], [0, .8]]), np.array([.1, 0])),
    (np.array([[.8, 0], [0, .8]]), np.array([.1, .1])),
    (np.array([[.8, 0], [0, .8]]), np.array([-.1, .1]))]

# Erstellung von Punktliste mit 3 Punkten, die die Eckpunkte eines beliebigen rechtwinkeligen Dreiecks darstellen
points = [np.array([0.4, 0.3])]

# Seperate Speicherung der Startpunkte
start_points = points.copy()
# Anzahl der Iterationen
iterations = 10**6
# Für jeden Iterationsschritt wird entweder der Mittelpunkt von 3 oder von 2 Punkten gebildet,
current_point = points[0]
for i in range(iterations):
    current_point = affine(current_point, *random.choice(transforms))
    points.append(current_point)

# Extrahieren von Informationen für Plots
x, y = [i[0] for i in points], [i[1] for i in points]
# Scatterplot erstellen und anzeigen
plt.scatter(x, y,s=1, color='blue')
# plt.plot(x,y)
plt.axis('equal')
plt.show()
