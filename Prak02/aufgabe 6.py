from libcfcg import cf
import numpy as np
import sys


class Ant:
    movement_map = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

    def __init__(self, pos: cf.Point, direction: int = 0, color: cf.Color = cf.Color.RED):
        # There are only 4 legal directions for the ant
        assert direction in [0, 1, 2, 3]  # 0 = up, 1=right, 2=down, 3=left
        self.position = pos
        self.direction = direction
        self.color = color

    def move(self, field: np.ndarray, win: cf.WindowRasterized) -> np.ndarray:
        if field[int(self.position.x), int(self.position.y)]:
            win.setColor(int(self.position.x), int(self.position.y), cf.Color.WHITE)
            field[int(self.position.x), int(self.position.y)] = 0
            self.direction += 1
            self.direction = self.direction % 4
            self.position = cf.Point(int(self.position.x) + self.movement_map[self.direction][0],
                                     int(self.position.y) + self.movement_map[self.direction][1])
        else:
            win.setColor(int(self.position.x), int(self.position.y), self.color)
            field[int(self.position.x), int(self.position.y)] = 1
            self.direction += 3
            self.direction = self.direction % 4
            self.position = cf.Point(int(self.position.x) + self.movement_map[self.direction][0],
                                     int(self.position.y) + self.movement_map[self.direction][1])
        sys.stdout.flush()
        win.show()
        return field


if __name__ == '__main__':
    i_range,j_range = 101, 101
    n_iter,n_test = int(1.5 * 10 ** 4), 10 ** 4
    first_field = np.zeros((i_range, j_range))
    # image corresponding to the 2D float interval
    window = cf.WindowRasterized(i_range, j_range, "Aufgabe 6", cf.Color.WHITE)
    window.setWindowDisplayScale(8.0)
    window.show()
    ant1 = Ant(cf.Point(i_range // 2, j_range // 2))
    ant2 = Ant(cf.Point(i_range // 2, j_range // 4), color=cf.Color.GREEN, direction=2)
    for i in range(n_test):
        first_field = ant1.move(first_field, window)
        first_field = ant2.move(first_field, window)
    window.waitKey()
