# Importiere erforderliche Bibliotheken
from library.libcfcg import cf
import sys
import time
import random
from typing import List


# Funktion zur Erfassung von Mausklick-Punkten
def get_points(window: cf.WindowRasterized) -> List[cf.Point]:
    # Definiere Farben für die Punkte
    colors = [cf.Color.YELLOW, cf.Color.RED, cf.Color.WHITE, cf.Color.CYAN]
    points = []

    # Erfasse 4 Mausklick-Punkte
    for i in range(4):
        point = window.waitMouseInput()  # Warte auf Maus-Eingabe
        points.append(point)
        window.drawCircle(point, 3, -1, colors[i])  # Zeichne einen sichtbaren Kreis um den Punkt
        sys.stdout.flush()
        window.show()

    return points


# Funktion für eine Iteration des Fraktalalgorithmus
def iteration(start_point: cf.Point, points: List[cf.Point], window: cf.WindowRasterized) -> cf.Point:
    # Wähle zufällig einen Punkt aus der Liste
    chosen_one = random.choice(points)

    # Berechne den Mittelpunkt zwischen dem ausgewählten Punkt und dem aktuellen Startpunkt
    point = cf.Point((chosen_one.x + start_point.x) / 2, (chosen_one.y + start_point.y) / 2)

    # Zeichne einen sichtbaren Kreis um den neuen Punkt mit einer zufälligen Farbe
    window.drawCircle(point, 3, -1, cf.Color_RandomColor())

    return point


# Hauptprogramm
if __name__ == '__main__':
    # Anzahl der Iterationen
    n_iter = 10 ** 4

    # Dimensionen des Fensters
    i_range = 750
    j_range = 750

    # Initialisiere eine leere Liste für die Punkte
    points = []

    # Erstelle ein Fensterobjekt
    window = cf.WindowRasterized(i_range, j_range, "CF_1_1")

    # Setze die Anzeigeskala
    window.setWindowDisplayScale(512 / i_range)

    # Zeige das Fenster an
    window.show()

    # Gib eine Benutzeranweisung aus
    print("Use mouse to set 4 points")

    # Erfasse 4 Mausklick-Punkte
    points = get_points(window)

    # Setze den Startpunkt als den zuletzt erfassten Punkt
    start_point = points[-1]

    # Verwende nur die ersten 3 erfassten Punkte
    points = points[:3]

    # Führe den Fraktalalgorithmus für die angegebene Anzahl von Iterationen durch
    for i in range(n_iter):
        start_point = iteration(start_point, points, window)

        # Zeige das Fenster alle 100 Iterationen, um den Fortschritt zu sehen
        if i % 100 == 0:
            sys.stdout.flush()
            window.show()

    # Warte auf eine Benutzereingabe, bevor das Programm endet
    window.waitKey()
