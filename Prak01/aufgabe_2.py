# Importiere erforderliche Bibliotheken
from libcfcg import cf
import numpy as np
import csv
from typing import List
import os


# Funktion zum Lesen einer Look-up-Tabelle (LUT) aus einer CSV-Datei
def readLut(filepath: str) -> List[List[str]]:
    lut = []
    # Öffne die CSV-Datei
    with open(filepath, 'r') as f:
        # Verwende csv.reader, um die Farbwerte zu lesen
        reader = csv.reader(f, delimiter=',', quotechar='\n')
        for color in reader:
            lut.append(color)
    return lut


# Hauptprogramm
if __name__ == '__main__':
    # Definiere den Dateipfad zur LUT-Datei
    lutFile = '../library/chaos_files/Multcol4.pal'

    # Lese die LUT aus der CSV-Datei
    lut = readLut(lutFile)

    # Definiere die Dimensionen des Fensters
    i_range, j_range = 256, 256

    # Erstelle ein Fensterobjekt
    window = cf.WindowRasterized(i_range, j_range, "CF_1_1")

    # Setze die Anzeigeskala
    window.setWindowDisplayScale(512 / i_range)

    # Erstelle Arrays für die x- und y-Koordinaten
    x_arr, y_arr = [i for i in range(i_range)], [i for i in range(j_range)]

    # Erstelle eine 2D-Liste, indem jedes Element das Ergebnis von i & j ist
    arr_final = [[i & j for j in y_arr] for i in x_arr]

    # Kopiere arr_final in die Variable colors
    colors = arr_final.copy()

    # Konvertiere arr_final und colors in Tuple-Formate
    arr_final = tuple(tuple((i, j) for j in y_arr) for i in x_arr)

    # Erstelle ein Dictionary (cmap), das Punkte auf Farben abbildet
    cmap = {point: col for point, col in zip(arr_final, colors)}

    # Flache die Liste von Punkten ab
    points = [[i for i in j] for j in arr_final]
    p = []
    for i in points:
        p += i
    points = p

    # Setze die Farben im Fenster basierend auf der LUT und den Punkten
    for i in cmap:
        for j in i:
            col = lut[j[0] & j[1]]
            window.setColor(j[0], j[1], cf.Color(int(col[0]), int(col[1]), int(col[2])))

    # Zeige das Fenster an
    window.show()

    # Warte auf eine Benutzereingabe, bevor das Programm endet
    window.waitKey()
