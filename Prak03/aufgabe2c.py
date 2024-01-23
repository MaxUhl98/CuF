import sys

from libcfcg import cf
import numpy as np

if __name__ == '__main__':
    n_iter = 2 * 10 ** 4
    # Irgendwie ist mit den Koordinaten aus der Aufgabe der Attraktor nicht vollständig sichtbar
    win = cf.WindowVectorized(512, cf.Interval(-12, 15), cf.Interval(-8, 25))
    a, b, c = .2, .2, 5.7
    x_old, y_old, z_old = 1, 1, 1
    x_new, y_new, z_new = 1, 1, 1

    dt = .04
    for i in range(n_iter):
        x_diff = -(y_old + z_old)
        y_diff = a * y_old + x_old
        z_diff = b + x_old * z_old - c * z_old

        x_new += x_diff * dt
        y_new += y_diff * dt
        z_new += z_diff * dt

        x_diff = -(y_new + z_new)
        y_diff = a * y_new + x_new
        z_diff = b + x_new * z_new - c * z_new

        x_new = .5 * x_old + .5 * (x_new + dt * x_diff)
        y_new = .5 * y_old + .5 * (y_new + dt * y_diff)
        z_new = .5 * z_old + .5 * (z_new + dt * z_diff)

        if i >= 1000:
            print([x_old, y_old, z_old])
            print([x_new, y_new, z_new])
            win.drawLine(cf.Point(x_old, y_old / 2 + z_old), cf.Point(x_new, y_new / 2 + z_old), 1,
                         cf.Color.RandomColor())

            if i % 25:
                sys.stdout.flush()
                win.show()

        x_old, y_old, z_old = x_new, y_new, z_new
