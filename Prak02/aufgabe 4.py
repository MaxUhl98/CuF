from libcfcg import cf, helper
import numpy as np
import random as r
import sys

def iteration(point: cf.Point, transform: np.ndarray, col: cf.Color) -> cf.Point:
    """
    Führt eine Iteration des Iterated Function Systems (IFS) durch.

    Parameters:
    - point (cf.Point): Der aktuelle Punkt im Koordinatensystem.
    - transform (np.ndarray): Die Transformationsmatrix für die Iteration.
    - col (cf.Color): Die aktuelle Farbe für den Punkt.

    Returns:
    - cf.Point: Der neue Punkt nach der Iteration.
    """
    # Konvertiere den Punkt zu einem numpy-Array für die Matrixmultiplikation
    point = np.array([point.x, point.y, 1])
    # Wende die Transformation auf den Punkt an
    new_point = transform @ point
    # Erstelle einen neuen Punkt und setze die Farbe im Fenster
    new_point = cf.Point(new_point[0], new_point[1])
    window.setColor(new_point.x, new_point.y, color=col)
    return new_point

def get_probabilities(transforms: np.ndarray) -> np.ndarray:
    """
    Berechnet die Wahrscheinlichkeiten für die Auswahl jeder Transformation.

    Parameters:
    - transforms (np.ndarray): Eine Matrix von Transformationsmatrizen.

    Returns:
    - np.ndarray: Ein Array von Wahrscheinlichkeiten für jede Transformation.
    """
    full_sum = sum([abs(t[0, 0] * t[1, 1] - t[0, 1] * t[1, 0]) for t in transforms])
    return np.array(
        [abs(t[0, 0] * t[1, 1] - t[0, 1] * t[1, 0]) if abs(t[0, 0] * t[1, 1] - t[0, 1] * t[1, 0]) != 0 else 0.01 for t
         in transforms]) / full_sum

if __name__ == '__main__':
    # Konstanten für die Iteration
    i_range = 512
    j_range = 512
    n_iter = int(1.5 * 10 ** 4)
    points = []
    filename = 'TEST_IFS.IFS'

    # Initialisiere das Iterated Function System (IFS) und lese die Datei ein
    ifs = cf.IteratedFunctionSystem()
    ifs.read(f"{filename}")

    # Erzeuge eine Matrix aus den Transformationsmatrizen des IFS
    transforms = np.array(
        [helper.convertMat3x3ToArray(ifs.getTransformation(i)) for i in range(ifs.getNumTransformations())])

    # Festlegung der Intervalle für x- und y-Koordinaten
    xInt = [ifs.getRangeX().getMin(), ifs.getRangeX().getMax()]
    yInt = [ifs.getRangeY().getMin(), ifs.getRangeY().getMax()]
    cfIntervalX = cf.Interval(xInt[0], xInt[1])
    cfIntervalY = cf.Interval(yInt[0], yInt[1])

    # Berechne die Wahrscheinlichkeiten für die Auswahl der Transformationen
    weights = get_probabilities(transforms)

    # Erstelle ein Fenster für die Visualisierung
    window = cf.WindowVectorized(512, cfIntervalX, cfIntervalY, "Window Vectorized example")
    window.setWindowDisplayScale(1.0)
    window.show()

    # Bestimme den Fixpunkt basierend auf der ersten Transformationsmatrix und setze ihn als Startpunkt
    tr = transforms[0]
    start_x = (-tr[0,2] * (tr[1,1] - 1) + tr[0,1] * tr[1,0]) / ((tr[0,0] - 1) * (tr[1,1] - 1)- tr[1,0]*tr[0,1])
    start_y = (-tr[1,2] * (tr[0,0] - 1) + tr[1,0] * tr[0,2]) / ((tr[0,0] - 1) * (tr[1,1] - 1)- tr[1,0]*tr[0,1])
    start_point = cf.Point(start_x, start_y)

    # Zufällige Farbe für die Iteration
    current_col = cf.Color_RandomColor()

    # Führe die Iteration durch und update das Fenster alle 100 Iterationen
    for _ in range(n_iter):
        # Wähle zufällig eine Transformation basierend auf den Wahrscheinlichkeiten aus
        transform = r.choices(transforms, weights=weights, k=1)[0]
        start_point = iteration(start_point, transform, current_col)
        if _ % 100 == 0:
            sys.stdout.flush()
            window.show()
            current_col = cf.Color_RandomColor()

    window.waitKey()
