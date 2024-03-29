from libcfcg import cf
import numpy as np
import sys
import random


class Ant:
    """Klasse die das Verhalten der Ameise aus der Aufgabe emuliert"""
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

    def move(self, field: np.ndarray, win: cf.WindowRasterized, win_size: int = 512) -> (np.ndarray, cf.WindowRasterized):
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


if __name__ == '__main__':
    # Erste Testkonfiguration
    i_range, j_range = 101, 101
    n_test, n_iter= 10, 10**7
    first_field = np.zeros((i_range, j_range))
    window = cf.WindowRasterized(i_range, j_range, "Aufgabe 6 Test", cf.Color.WHITE)
    window.setWindowDisplayScale(8.0)
    window.show()
    ant1 = Ant(cf.Point(i_range // 2, j_range // 2))
    ant2 = Ant(cf.Point(i_range // 2, j_range // 4), color=cf.Color.GREEN, direction=2)
    for _ in range(n_test):
        first_field, window = ant1.move(first_field, window)
        sys.stdout.flush()
        window.show()
    window.waitKey()

    # Zweite Testkonfiguration
    i_range, j_range = 512, 512
    window = cf.WindowRasterized(i_range, j_range, "Aufgabe 6", cf.Color.WHITE)
    window.setWindowDisplayScale(1.5)
    window.show()
    second_field = np.zeros((i_range, j_range))
    ant1 = Ant(cf.Point(random.randrange(0, 512), random.randrange(0, 512)), direction=random.randrange(0, 4))
    ant2 = Ant(cf.Point(random.randrange(0, 512), random.randrange(0, 512)), color=cf.Color.GREEN,
               direction=random.randrange(0, 4))
    for i in range(n_iter):
        second_field, window = ant1.move(second_field, window)
        second_field, window = ant2.move(second_field, window)
        if i % 100 == 0:
            sys.stdout.flush()
            window.show()
    window.waitKey()
