from library.libcfcg import cf
import sys
import time
import random
from typing import List, Tuple


# import numpy as np

def get_pascal_matrix(dim: Tuple[int]):
    assert dim[0] == dim[1] - 1
    mat = [[0 for _ in range(dim[1])] for _ in range(dim[0])]
    mat[0][1] = 1
    for i in range(1, dim[0]):
        for j in range(1, i + 2):
            mat[i][j] = mat[i - 1][j - 1] + mat[i - 1][j]
    return mat


def draw_pascal(arr: list, divider: int, win: cf.WindowRasterized):
    x, y = len(arr), len(arr[0])
    points = []
    for i in range(x):
        for j in range(y):
            # print(arr[i,j]%2)
            if arr[i][j] % divider != 0:
                points.append((i, j))
    return points


def draw_colors(matrix: list, ):
    pass


if __name__ == '__main__':
    i_range = 512
    j_range = 512
    dim = (512, 513)
    arr = get_pascal_matrix(dim)[:][1:]
    window = cf.WindowRasterized(i_range, j_range, "CF_1_1")
    window.setWindowDisplayScale(512 / i_range)
    points = draw_pascal(arr, 32, win=window)
    # print(arr)
    for i in points:
        window.setColor(i[0], i[1], cf.Color.RED)
    while 1:
        window.show()
