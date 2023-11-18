from library.libcfcg import cf
import sys
import time
import random
from typing import List


def get_points(window: cf.WindowRasterized):
    colors = [cf.Color.YELLOW, cf.Color.RED, cf.Color.WHITE, cf.Color.CYAN]
    points = []
    for i in range(4):
        point = window.waitMouseInput()
        points.append(point)
        window.drawCircle(point, 3, -1, colors[i])  # visible!!!
        sys.stdout.flush()
        window.show()
    return points


def iteration(start_point: cf.Point, points: List[cf.Point], window: cf.WindowRasterized):
    choosen_one = random.choice(points)
    point = cf.Point((choosen_one.x + start_point.x) / 2, (choosen_one.y + start_point.y) / 2)
    window.drawCircle(point, 3, -1, cf.Color_RandomColor())
    return point


if __name__ == '__main__':
    i_range = 750
    j_range = 750
    points = []
    window = cf.WindowRasterized(i_range, j_range, "CF_1_1")
    window.setWindowDisplayScale(512 / i_range)
    window.show()

    print("Use mouse to set 4 points")
    points = get_points(window)
    start_point = points[-1]
    points = points[:3]

    for i in range(10 ** 4):
        start_point = iteration(start_point, points, window)
        if i % 100 == 0:
            sys.stdout.flush()
            window.show()

    while 1:
        window.show()