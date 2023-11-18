# Importiere erforderliche Bibliotheken
from library.libcfcg import cf
import sys
import time
import random
from typing import List, Tuple


# Funktion zur Erzeugung einer modifizierten Pascal'schen Matrix
def get_pascal_matrix(dim: Tuple[int]) -> List[List[int]]:
    # Überprüfe, ob die Dimensionen korrekt sind
    assert dim[0] == dim[1] - 1

    # Initialisiere die Matrix mit Nullen
    mat = [[0 for _ in range(dim[1])] for _ in range(dim[0])]

    # Setze den Wert in der ersten Zeile und zweiten Spalte auf 1
    mat[0][1] = 1

    # Fülle die Matrix gemäß der Pascal'schen Regel
    for i in range(1, dim[0]):
        for j in range(1, i + 2):
            mat[i][j] = mat[i - 1][j - 1] + mat[i - 1][j]

    return mat


# Funktion zum Zeichnen von Punkten basierend auf einer Farbregel
def draw_pascal(arr: List[List[int]], divider: int, win: cf.WindowRasterized) -> List[Tuple[int, int]]:
    # Erhalte die Dimensionen der Matrix
    x, y = len(arr), len(arr[0])

    # Initialisiere eine Liste für die ausgewählten Punkte
    points = []

    # Durchlaufe die Matrix
    for i in range(x):
        for j in range(y):
            # Überprüfe die Farbregel und füge den Punkt zur Liste hinzu, wenn die Bedingung erfüllt ist
            if arr[i][j] % divider != 0:
                points.append((i, j))

    return points


# Funktion zum Zeichnen von Farben (noch nicht implementiert)
def draw_colors(matrix: list):
    pass


# Hauptprogramm
if __name__ == '__main__':
    # Definiere Fensterdimensionen
    i_range = 512
    j_range = 512

    # Definiere die Dimension der Pascal'schen Matrix
    dim = (512, 513)

    # Erhalte die modifizierte Pascal'sche Matrix
    arr = get_pascal_matrix(dim)[:][1:]

    # Erstelle ein Fensterobjekt
    window = cf.WindowRasterized(i_range, j_range, "CF_1_1")

    # Setze die Anzeigeskala
    window.setWindowDisplayScale(512 / i_range)

    # Erhalte die Punkte gemäß der Farbregel
    points = draw_pascal(arr, 32, win=window)

    # Setze die Farbe der ausgewählten Punkte auf Rot
    for i in points:
        window.setColor(i[0], i[1], cf.Color.RED)

    # Fenster anzeigen
    window.show()

    # Warte auf eine Benutzereingabe, bevor das Programm endet
    window.waitKey()
