import sys

from libcfcg import cf
import numpy as np

if __name__ == '__main__':
    n_iter = 2 * 10 ** 4
    # Irgendwie ist mit den Koordinaten aus der Aufgabe der Attraktor nicht vollständig sichtbar
    win = cf.WindowVectorized(512, cf.Interval(-22, 22), cf.Interval(-1, 55))
    a, b, c = 10, 2.667, 28
    x_old, y_old, z_old = 1, 1, 1
    x_new, y_new, z_new = 1, 1, 1

    dt = .01
    t = 0
    for i in range(n_iter):
        x_diff = a * y_old - a * x_old
        y_diff = c * x_old - y_old - x_old * z_old
        z_diff = x_old * y_old - b * z_old
        x_new += x_diff * dt
        y_new += y_diff * dt
        z_new += z_diff * dt

        if i >= 1000:
            win.drawLine(cf.Point(x_old, z_old), cf.Point(x_new,  z_new), 1,
                         cf.Color.RandomColor())

            if i % 25:
                sys.stdout.flush()
                win.show()

        x_old, y_old, z_old = x_new, y_new, z_new
