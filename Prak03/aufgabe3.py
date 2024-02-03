import sys
import time
from typing import Iterable
from libcfcg import cf
import numpy as np
import random


class Ant:
    movement_map = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}

    def __init__(self, pos: cf.Point, direction: int = 0, color: cf.Color = cf.Color.RED):
        """
        Initialisiert eine Ameise mit einer Position, Richtung und Farbe.

        Parameters:
        - pos (cf.Point): Die Startposition der Ameise.
        - direction (int): Die Startrichtung der Ameise (0=up, 1=right, 2=down, 3=left).
        - color (cf.Color): Die Farbe der Ameise.
        """
        assert direction in [0, 1, 2, 3]  # 0 = up, 1=right, 2=down, 3=left
        self.position = pos
        self.direction = direction
        self.color = color

    def movement_0(self, field: np.ndarray, win: cf.WindowRasterized, win_size: int = 512, n_states: int = 2,
                   col: cf.Color = cf.Color.RED):
        """
        Führt eine Bewegung der Ameise gemäß Regel 0 durch und aktualisiert das Feld und das Fenster.

        Parameters:
        - field (np.ndarray): Das Feld, auf dem sich die Ameise bewegt.
        - win (cf.WindowRasterized): Das Fenster, in dem die Ameise visualisiert wird.
        - win_size (int): Die Größe des Fensters.
        - n_states (int): Die Anzahl der Zustände.
        - col (cf.Color): Die Farbe der Ameise.
        """
        win.setColor(int(self.position.x), int(self.position.y), col)
        field[int(self.position.x), int(self.position.y)] += 1
        field[int(self.position.x), int(self.position.y)] %= n_states
        self.direction += 3
        self.direction = self.direction % 4
        self.position = cf.Point((int(self.position.x) + self.movement_map[self.direction][0]) % win_size,
                                 (int(self.position.y) + self.movement_map[self.direction][1]) % win_size)

    def movement_1(self, field: np.ndarray, win: cf.WindowRasterized, win_size: int = 512, n_states: int = 2,
                   col: cf.Color = cf.Color.GREEN):
        """
        Führt eine Bewegung der Ameise gemäß Regel 1 durch und aktualisiert das Feld und das Fenster.

        Parameters:
        - field (np.ndarray): Das Feld, auf dem sich die Ameise bewegt.
        - win (cf.WindowRasterized): Das Fenster, in dem die Ameise visualisiert wird.
        - win_size (int): Die Größe des Fensters.
        - n_states (int): Die Anzahl der Zustände.
        - col (cf.Color): Die Farbe der Ameise.
        """
        win.setColor(int(self.position.x), int(self.position.y), col)
        field[int(self.position.x), int(self.position.y)] += 1
        field[int(self.position.x), int(self.position.y)] %= n_states
        self.direction += 1
        self.direction = self.direction % 4
        self.position = cf.Point((int(self.position.x) + self.movement_map[self.direction][0]) % win_size,
                                 (int(self.position.y) + self.movement_map[self.direction][1]) % win_size)

    def move(self, field: np.ndarray, win: cf.WindowRasterized, win_size: int = 512) -> (
    np.ndarray, cf.WindowRasterized):
        """
        Führt einen Schritt der Ameise auf dem Feld durch und aktualisiert das Feld und das Fenster.

        Parameters:
        - field (np.ndarray): Das Feld, auf dem sich die Ameise bewegt.
        - win (cf.WindowRasterized): Das Fenster, in dem die Ameise visualisiert wird.
        - win_size (int): Die Größe des Fensters.

        Returns:
        - np.ndarray: Das aktualisierte Feld.
        - cf.WindowRasterized: Das aktualisierte Fenster.
        """
        if field[int(self.position.x), int(self.position.y)] == 1:
            self.movement_1(field, win, win_size)
        else:
            self.movement_0(field, win, win_size)
        return field, win

    def move_string(self, field: np.ndarray, win: cf.WindowRasterized, movement_code: str, color_palette: Iterable,
                    win_size: int = 512):
        """
        Führt einen Schritt der Ameise auf dem Feld durch, basierend auf einem Bewegungscode, und aktualisiert das Feld und das Fenster.

        Parameters:
        - field (np.ndarray): Das Feld, auf dem sich die Ameise bewegt.
        - win (cf.WindowRasterized): Das Fenster, in dem die Ameise visualisiert wird.
        - movement_code (str): Der Bewegungscode, der die Ameisenbewegung bestimmt.
        - color_palette (Iterable): Die Farbpalette für die Ameise.
        - win_size (int): Die Größe des Fensters.
        """
        if int(movement_code[::-1][int(field[int(self.position.x), int(self.position.y)])]) == 1:
            self.movement_1(field, win, n_states=len(movement_code), win_size=win_size,
                            col=color_palette[int(field[int(self.position.x), int(self.position.y)])])
        else:
            self.movement_0(field, win, n_states=len(movement_code), win_size=win_size,
                            col=color_palette[int(field[int(self.position.x), int(self.position.y)])])
        return field, win


def loadColorsFromPalFile(path: str) -> list[cf.Color]:
    """
    Lädt Farben aus einer PAL-Datei.

    :param path: Der Pfad zur PAL-Datei.
    :return: Eine Liste von cf.Color-Objekten aus der PAL-Datei.
    """
    file = open(path)
    colors = []
    while True:
        line = file.readline()
        if len(line) == 0:
            break

        s = line.split(',')
        colors.append(cf.Color(int(s[0]), int(s[1]), int(s[2])))

    file.close()
    return colors


if __name__ == '__main__':
    n_iter = 10 ** 7
    i_range, j_range = 512, 512
    window = cf.WindowRasterized(i_range, j_range, "Aufgabe 6", cf.Color.WHITE)
    window.setWindowDisplayScale(1.5)
    window.show()
    second_field = np.zeros((i_range, j_range))
    ant1 = Ant(cf.Point(random.randrange(0, 512), random.randrange(0, 512)), direction=random.randrange(0, 4))
    value = cf.readAntString('../library/chaos_files/Ant_14.ant')
    colors = loadColorsFromPalFile("../library/chaos_files/Chaos_ant.pal")
    for i in range(n_iter):
        second_field, window = ant1.move_string(second_field, window, value, colors)
        if i % 100 == 0:
            sys.stdout.flush()
            window.show()
    window.waitKey()
