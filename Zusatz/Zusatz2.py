from typing import Union
import numpy as np


def iterator(_x: Union[float, int], _r: Union[float, int]) -> Union[float, int]:
    return _r * _x - _r * _x ** 2


if __name__ == '__main__':
    n_iter = 10 ** 5
    info = np.ones(n_iter)
    x = 0.01
    r = 1
    for i in range(n_iter):
        x = iterator(x, r)
        info[i] = x
    print(info)

