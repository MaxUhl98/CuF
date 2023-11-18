from library.libcfcg import cf
import numpy as np
import csv

if __name__ == '__main__':
    lutFile = 'library/chaos_files/Multcol4.pal'


    def readLut():
        lut = []
        f = open(lutFile, 'r')
        reader = csv.reader(f, delimiter=',', quotechar='\n')
        for color in reader:
            lut.append(color)
        return lut


    lut = readLut()
    i_range, j_range = 256, 256
    window = cf.WindowRasterized(i_range, j_range, "CF_1_1")
    window.setWindowDisplayScale(512 / i_range)
    x_arr, y_arr = [i for i in range(i_range)], [i for i in range(j_range)]
    arr_final = [[i & j for j in y_arr] for i in x_arr]
    colors = arr_final.copy()
    arr_final = tuple(tuple((i, j) for j in y_arr) for i in x_arr)
    cmap = {point: col for point, col in zip(arr_final, colors)}
    points = [[i for i in j] for j in arr_final]
    p = []
    for i in points:
        p += i
    points = p
    for i in cmap:
        for j in i:
            col = lut[j[0] & j[1]]

            window.setColor(j[0], j[1], cf.Color(int(col[0]), int(col[1]),
                                                 int(col[2])))
    while 1:
        window.show()
