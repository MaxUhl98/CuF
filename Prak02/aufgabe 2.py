from libcfcg import cf, helper
import numpy as np
import random as r
import sys


def iteration(point: cf.Point, transform: np.ndarray, col: cf.Color) -> cf.Point:
    point = np.array([point.x, point.y, 1])
    new_point = transform @ point
    new_point = cf.Point(new_point[0], new_point[1])
    window.setColor(new_point.x,new_point.y,color=col)
    return new_point

def get_probabilities(transforms:np.ndarray) -> np.ndarray:
    full_sum = sum([abs(t[0,0]*t[1,1]-t[0,1]*t[1,0]) for t in transforms])
    return np.array([abs(t[0,0]*t[1,1]-t[0,1]*t[1,0]) if abs(t[0,0]*t[1,1]-t[0,1]*t[1,0]) != 0 else 0.01 for t in transforms])/full_sum

if __name__ == '__main__':
    i_range = 512
    j_range = 512
    n_iter = int(1.5 * 10 ** 4)
    points = []
    filename = 'Strauch.ifs'

    ifs = cf.IteratedFunctionSystem()
    ifs.read(f"../library/chaos_files/{filename}")

    transforms = np.array([helper.convertMat3x3ToArray(ifs.getTransformation(i)) for i in range(ifs.getNumTransformations())])
    #transforms = np.array([[[.5, 0, 0], [0, .5, 0], [0, 0, 1]], [[.5, 0, .5], [0, .5, 0], [0, 0, 1]],
    #                       [[.5, 0, 0], [0, .5, .5], [0, 0, 1]]])
    xInt = [ifs.getRangeX().getMin(), ifs.getRangeX().getMax()]
    yInt =[ifs.getRangeY().getMin(), ifs.getRangeY().getMax()]
    cfIntervalX = cf.Interval(xInt[0], xInt[1])
    cfIntervalY = cf.Interval(yInt[0], yInt[1])
    weights = get_probabilities(transforms)
    print(weights)
    # image corresponding to the 2D float interval
    window = cf.WindowVectorized(512, cfIntervalX, cfIntervalY,
                                 "Window Vectorized example")
    window.setWindowDisplayScale(1.0)
    window.show()
    start_point = cf.Point(1, 1)
    current_col = cf.Color_RandomColor()
    for _ in range(n_iter):
        transform = r.choices(transforms,weights=weights,k=1)[0]
        start_point = iteration(start_point, transform, current_col)
        if _ % 100 == 0:
            sys.stdout.flush()
            window.show()
            current_col = cf.Color_RandomColor()
    window.waitKey()
