from python_lab.libcfcg import cf
import sys
import time
import random
from typing import List,Tuple
import numpy as np

def get_pascal_matrix(dim:Tuple[int]):
    assert dim[0] == dim[1]-1
    mat = np.zeros(dim)
    mat[0,1] = 1
    for i in range(1,dim[0]):
        for j in range(1,i+2):
            mat[i,j] = mat[i-1,j-1] + mat[i-1,j]
    return  mat

def draw_colors(matrix:np.ndarray, ):
    pass

if __name__ == '__main__':
    i_range = 750
    j_range = 750
    dim = (9,10)
    print(get_pascal_matrix(dim))
    #window = cf.WindowRasterized(i_range, j_range, "CF_1_1")
    #window.setWindowDisplayScale(512 / i_range)
    #window.show()



