from libcfcg import cf, helper
import numpy as np
import random as r
import sys
import numpy as np


def iteration(point: cf.Point, transformation: np.ndarray, col: cf.Color) -> cf.Point:
    point = np.array([point.x, point.y, 1])
    new_point = r.choice(transforms) @ point
    new_point = cf.Point(new_point[0], new_point[1])
    window.setColor(new_point.x, new_point.y, color=col)
    return new_point


if __name__ == '__main__':
    i_range = 512
    j_range = 512
    n_iter = int(1.5 * 10 ** 4)
    divergence_threshold = 10 ** 4
    points = []
    filename = 'INVERSES_TEST_IFS.IFS'
    ifs = cf.IteratedFunctionSystem()
    ifs.read(f"{filename}")
    transforms = np.array(
        [helper.convertMat3x3ToArray(ifs.getTransformation(i)) for i in range(ifs.getNumTransformations())])
    transforms = np.array(
        [helper.convertMat3x3ToArray(ifs.getTransformation(i)) for i in range(ifs.getNumTransformations())])
    xInt = [ifs.getRangeX().getMin(), ifs.getRangeX().getMax()]
    yInt = [ifs.getRangeY().getMin(), ifs.getRangeY().getMax()]
    cfIntervalX = cf.Interval(xInt[0], xInt[1])
    cfIntervalY = cf.Interval(yInt[0], yInt[1])

    # image corresponding to the 2D float interval
    window = cf.WindowRasterized(i_range,j_range,
                                 "Window Vectorized example")
    window.setWindowDisplayScale(1.0)
    window.show()
    start_point = cf.Point(1, 1)
    current_col = cf.Color_RandomColor()
    window_points = np.zeros((i_range, j_range))
    for x in range(i_range):
        for y in range(j_range):
            val = np.array([x / i_range, y / j_range, 1])
            for _ in range(15):
                if val[0] <= .5 and val[1] <= .5:
                    val = transforms[0] @ val
                elif val[0] > .5 and val[1] <= .5:
                    val = transforms[1] @ val
                else:
                    val = transforms[2] @ val
                if val[0] ** 2 + val[1] ** 2 >= divergence_threshold:
                    break
                if _ == 14:
                    window.setColor(x,511-y,cf.Color.RED)
        if x % 10 == 0:
            sys.stdout.flush()
            window.show()



    window.waitKey()
