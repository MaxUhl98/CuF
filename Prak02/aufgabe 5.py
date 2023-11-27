from libcfcg import cf, helper
import numpy as np
import random as r
import sys
import numpy as np

def iteration(point: cf.Point, transformation:np.ndarray, col: cf.Color) -> cf.Point:
    point = np.array([point.x, point.y, 1])
    new_point = r.choice(transforms) @ point
    new_point = cf.Point(new_point[0], new_point[1])
    window.setColor(new_point.x, new_point.y, color=col)
    return new_point


if __name__ == '__main__':
    i_range = 512
    j_range = 512
    n_iter = int(1.5 * 10 ** 4)
    points = []
    filename = 'Invers.ifs'
    ifs = cf.IteratedFunctionSystem()
    ifs.read(f"../library/chaos_files/{filename}")
    transforms = np.array(
        [helper.convertMat3x3ToArray(ifs.getTransformation(i)) for i in range(ifs.getNumTransformations())])
    transforms = np.array(
        [helper.convertMat3x3ToArray(ifs.getTransformation(i)) for i in range(ifs.getNumTransformations())])
    xInt = [ifs.getRangeX().getMin(), ifs.getRangeX().getMax()]
    yInt = [ifs.getRangeY().getMin(), ifs.getRangeY().getMax()]
    cfIntervalX = cf.Interval(xInt[0], xInt[1])
    cfIntervalY = cf.Interval(yInt[0], yInt[1])

    # image corresponding to the 2D float interval
    window = cf.WindowRasterized(512, cfIntervalX, cfIntervalY,
                                 "Window Vectorized example")
    window.setWindowDisplayScale(1.0)
    window.show()
    start_point = cf.Point(1, 1)
    current_col = cf.Color_RandomColor()
    for x in range(i_range):
        for y in range(j_range):
            val = np.array([x,y])
            for _ in range(15):
                if val[0] <= .5 and val[1] <= .5 :

    window.waitKey()
