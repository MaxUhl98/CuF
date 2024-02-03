from libcfcg import cf, helper
import numpy as np
import random as r
import sys

def iteration(point: cf.Point, transforms: np.ndarray, col: cf.Color) -> cf.Point:
    """
    Führt eine Iteration des Iterated Function Systems (IFS) durch.

    Parameters:
    - point (cf.Point): Der aktuelle Punkt im Koordinatensystem.
    - transforms (np.ndarray): Eine Matrix von Transformationen im IFS.
    - col (cf.Color): Die aktuelle Farbe für den Punkt.

    Returns:
    - cf.Point: Der neue Punkt nach der Iteration.
    """
    # Konvertiere den Punkt zu einem numpy-Array für die Matrixmultiplikation
    point = np.array([point.x, point.y, 1])
    # Wähle zufällig eine Transformation aus und wende sie auf den Punkt an
    new_point = r.choice(transforms) @ point
    # Erstelle einen neuen Punkt und setze die Farbe im Fenster
    new_point = cf.Point(new_point[0], new_point[1])
    window.setColor(new_point.x, new_point.y, color=col)
    return new_point

if __name__ == '__main__':
    # Konstanten für die Iteration
    i_range = 512
    j_range = 512
    n_iter = int(1.5 * 10 ** 5)
    points = []
    filename = 'Farn_1.ifs'

    # Initialisiere das Iterierte FunktionenSystem (IFS) und lese die Datei ein
    ifs = cf.IteratedFunctionSystem()
    ifs.read(f"../library/chaos_files/{filename}")

    # Erzeuge eine Matrix aus den Transformationsmatrizen des IFS
    transforms = np.array([helper.convertMat3x3ToArray(ifs.getTransformation(i)) for i in range(ifs.getNumTransformations())])

    # Festlegung der Intervalle für x- und y-Koordinaten
    xInt = [ifs.getRangeX().getMin(), ifs.getRangeX().getMax()]
    yInt = [ifs.getRangeY().getMin(), ifs.getRangeY().getMax()]
    cfIntervalX = cf.Interval(xInt[0], xInt[1])
    cfIntervalY = cf.Interval(yInt[0], yInt[1])

    # Erstelle ein Fenster für die Visualisierung
    window = cf.WindowVectorized(512, cfIntervalX, cfIntervalY, "Window Vectorized example")
    window.setWindowDisplayScale(1.0)
    window.show()

    # Startpunkt und erste Farbe für die Iteration festlegen
    start_point = cf.Point(0,0)
    current_col = cf.Color_RandomColor()

    # Führe die Iteration durch und update das Fenster alle 100 Iterationen
    for _ in range(n_iter):
        start_point = iteration(start_point, transforms, current_col)
        if _ % 100 == 0:
            sys.stdout.flush()
            window.show()
            current_col = cf.Color_RandomColor()

    window.waitKey()
