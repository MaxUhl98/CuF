import numpy as np
import matplotlib.pyplot as plt
import random

#Funktion die den Mittelpunkt von 2 Punkten berechnet
def middle(x1, x2):
    return np.array([(x1[0] + x2[0]) / 2, (x1[1] + x2[1]) / 2])

#Funktion die den Mittelpunkt von 3 Punkten berechnet
def middle3(x1, x2, x3):
    return np.array([(x1[0] + x2[0] + x3[0]) / 3, (x1[1] + x2[1] + x3[1]) / 3])



# Erstellung von Punktliste mit 3 Punkten, die die Eckpunkte eines beliebigen rechtwinkeligen Dreiecks darstellen
points = [np.array([1.0, 0.0]), np.array([0., 1.]), np.array([0, 0])]

# Seperate Speicherung der Startpunkte
start_points = points.copy()
# Anzahl der Iterationen
iterations = 100000



# Für jeden Iterationsschritt wird entweder der Mittelpunkt von 3 oder von 2 Punkten gebildet,
current_point = points[0]
for i in range(iterations):
    transform = random.randint(0, 1)
    if transform:
        # Mittelpunkt zwischen neustem Punkt und 2 Zufällig gewählten Punkten bilden
        current_point = middle3(current_point, random.choice(points), random.choice(points))
    else:
        # Mittelpunt von jetztigem Punkt und Zufälligem Startpunkt bilden
        current_point = middle(current_point, random.choice(start_points))
    # Punkt zu Punktmenge hinzufügen
    points.append(current_point)


#Extrahieren von Informationen für Plots
x, y = [i[0] for i in points], [i[1] for i in points]
# Scatterplot erstellen und anzeigen
plt.scatter(x, y, s=1, color='blue')
#plt.plot(x,y)
plt.axis('equal')
plt.show()
