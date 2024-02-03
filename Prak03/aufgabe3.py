import sys

from libcfcg import cf
import numpy as np


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

    def move(self, field: np.ndarray, win: cf.WindowRasterized, win_size: int = 512) -> (
            np.ndarray, cf.WindowRasterized):
        """
        Führt einen Schritt der Ameise auf dem Feld durch.

        Parameters:
        - field (np.ndarray): Das Feld, auf dem sich die Ameise bewegt.
        - win (cf.WindowRasterized): Das Fenster, in dem die Ameise visualisiert wird.
        - win_size (int): Die Größe des Fensters.

        Returns:
        - np.ndarray: Das aktualisierte Feld.
        - cf.WindowRasterized: Das aktualisierte Fenster.
        """
        if field[int(self.position.x), int(self.position.y)]:
            win.setColor(int(self.position.x), int(self.position.y), cf.Color.WHITE)
            field[int(self.position.x), int(self.position.y)] = 0
            self.direction += 1
            self.direction = self.direction % 4
            self.position = cf.Point((int(self.position.x) + self.movement_map[self.direction][0]) % win_size,
                                     (int(self.position.y) + self.movement_map[self.direction][1]) % win_size)
        else:
            win.setColor(int(self.position.x), int(self.position.y), self.color)
            field[int(self.position.x), int(self.position.y)] = 1
            self.direction += 3
            self.direction = self.direction % 4
            self.position = cf.Point((int(self.position.x) + self.movement_map[self.direction][0]) % win_size,
                                     (int(self.position.y) + self.movement_map[self.direction][1]) % win_size)
        return field, win

    def move_string(self, movement_string: str, win: cf.WindowRasterized, win_size: int = 512):
        for move in movement_string[::-1]:
            if move == '0':
                win.setColor(int(self.position.x), int(self.position.y), self.color)
                self.direction += 1
                self.direction = self.direction % 4
                self.position = self.position = cf.Point(
                    (int(self.position.x) + self.movement_map[self.direction][0]) % win_size,
                    (int(self.position.y) + self.movement_map[self.direction][1]) % win_size)
            else:
                win.setColor(int(self.position.x), int(self.position.y), self.color)
                self.direction += 3
                self.direction = self.direction % 4
                self.position = self.position = cf.Point(
                    (int(self.position.x) + self.movement_map[self.direction][0]) % win_size,
                    (int(self.position.y) + self.movement_map[self.direction][1]) % win_size)



if __name__ == '__main__':
    i_range, j_range = 512, 512
    window = cf.WindowRasterized(i_range, j_range, "Aufgabe 6", cf.Color.WHITE)
    window.setWindowDisplayScale(1.5)
    window.show()
    value = cf.readAntString('../library/chaos_files/Ant_6.ant')
    movement_order = value
    print(type(value))
    print(value)
    ant = Ant(cf.Point(5, 5))
    for i in range(10 ** 6):
        ant.move_string(value, window)
        if i % 10**4 == 0:
            print(i)
            sys.stdout.flush()
            window.show()

    while 1:
        window.show()
