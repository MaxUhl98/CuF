from libcfcg import cf, helper
import numpy as np
import random as r
import sys

def iteration(point: cf.Point, transformation: np.ndarray, col: cf.Color) -> cf.Point:
    """
    Führt eine Iteration des Iterated Function Systems (IFS) durch.

    Parameters:
    - point (cf.Point): Der aktuelle Punkt im Koordinatensystem.
    - transformation (np.ndarray): Die Transformationsmatrix für die Iteration.
    - col (cf.Color): Die aktuelle Farbe für den Punkt.

    Returns:
    - cf.Point: Der neue Punkt nach der Iteration.
    """
    # Konvertiere den Punkt zu einem numpy-Array für die Matrixmultiplikation
    point = np.array([point.x, point.y, 1])
    # Wende die Transformation auf den Punkt an
    new_point = transformation @ point
    # Erstelle einen neuen Punkt und setze die Farbe im Fenster
    new_point = cf.Point(new_point[0], new_point[1])
    window.setColor(new_point.x, new_point.y, color=col)
    return new_point

if __name__ == '__main__':
    i_range = 512
    j_range = 512
    n_iter = int(1.5 * 10 ** 4)
    divergence_threshold = 10**4
    points = []
    filename = 'INVERSES_TEST_IFS.IFS'

    # Initialisiere das Iterated Function System (IFS) und lese die Datei
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

    # Erstelle ein Fenster für die Visualisierung
    window = cf.WindowRasterized(i_range, j_range, "Window Vectorized example")
    window.setWindowDisplayScale(1.0)
    window.show()

    # Initialisierung von Startpunkt und Farbe
    start_point = cf.Point(1, 1)
    current_col = cf.Color_RandomColor()

    # Array zur Speicherung der Punkte im Fenster
    window_points = np.zeros((i_range, j_range))

    # Iteriere durch den Bildbereich
    for x in range(i_range):
        for y in range(j_range):
            val = np.array([x / i_range, y / j_range, 1])

            # Führe Iteration für jeden Punkt durch
            for _ in range(15):
                if val[0] <= .5 and val[1] <= .5:
                    val = transforms[0] @ val
                elif val[0] > .5 and val[1] <= .5:
                    val = transforms[1] @ val
                else:
                    val = transforms[2] @ val

                # Überprüfe auf Divergenz
                if val[0] ** 2 + val[1] ** 2 >= divergence_threshold:
                    break

                # Setze Farbe im Fenster für divergente Punkte
                if _ == 14:
                    window.setColor(x, 511 - y, cf.Color.RED)

                # Update das Fenster alle 100 Iterationen
                if (x+y) % 500 == 0:
                    sys.stdout.flush()
                    window.show()

    window.waitKey()
