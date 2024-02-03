import sys

from libcfcg import cf, helper
import numpy as np


def mySign(value):  # difference to NumPy:  mySign(0)=1    !!!
    if value < 0:
        return -1
    return 1


if __name__ == '__main__':
    filename = "Henon.orb"
    henon_changer = -1
    orb = cf.Orbit()
    orb.read(f'../library/chaos_files/{filename}')
    x_interval, y_interval = cf.Interval(orb.getRangeX().getMin(), orb.getRangeX().getMax()), cf.Interval(
        orb.getRangeY().getMin(), orb.getRangeY().getMax())
    win = cf.WindowVectorized(512, x_interval, y_interval)
    iteration_count = 0
    start_points = []
    startingPoints = orb.getAllStartingPoints()
    for sp in startingPoints:
        vec = helper.convertVec3ToArray(sp)
        vec = np.array(vec)
        start_points.append(vec)

    factors = orb.getAllFactors()
    all_factors = []
    for i in range(factors.size()):
        factor = factors[i]
        all_factors.append(factor)
    if 'Henon' in filename:
        all_factors[3] = henon_changer
    current_point = start_points[0][:2]
    #print(current_point)
    while 1:
        current_point = [
            all_factors[0] + all_factors[1] * current_point[1] + all_factors[2] * abs(current_point[0]) +
            all_factors[3] * (current_point[0] ** 2 + all_factors[4]) +
            mySign(current_point[0]) * all_factors[5]*np.sqrt(abs(all_factors[6]*current_point[0]+all_factors[7]))
            ,
            all_factors[8]+ all_factors[9]*current_point[0]]

        win.setColor(current_point[0], current_point[1], cf.Color.RandomColor())
        if iteration_count % 200 == 0 and iteration_count > 50:
            sys.stdout.flush()
            win.show()
            iteration_count = 200
        iteration_count += 1
        #breaker = win.waitKeyPressed(100)
        #if breaker != 255:
        #    break
