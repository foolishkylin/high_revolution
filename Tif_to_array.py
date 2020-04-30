# Author: luzeng
# Time:   2018/12/18
# Name:   Tif2array

from osgeo import gdal
import numpy as np


def read_tiff(filename_):
    # 打开遥感图像
    ds = gdal.Open(filename_)
    # print(ds)
    row = ds.RasterXSize
    col = ds.RasterYSize
    min_edge = min(row, col)  # 图片窄边
    proportion = 1  # 缩放比例
    if min_edge > 3000:
        proportion = 0.1
    elif 2000 < min_edge <= 3000:
        proportion = 0.2
    elif 1000 < min_edge <= 2000:
        proportion = 0.3
    elif 700 <= min_edge <= 1000:
        proportion = 0.4
    # 太大估计会越界

    row = int(row * proportion)
    col = int(col * proportion)

    print('row=',row)
    print('col=',col)
    # 波数
    band = ds.RasterCount
    print('band =',band)
    data = np.zeros([row, col, band])
    # 遍历每个波段
    for i in range(band):
        # 获得波段数,波段数即图像每个像素点所含的颜色种类
        dt = ds.GetRasterBand(1)
        data[:, :, i] = dt.ReadAsArray(0, 0, col, row)
    return data, band

def array2rgb(filename_):
    data, band = read_tiff(filename_)
    # 最后一个维度是波段
    print('data.shape=',data.shape)
    # print(data[:, :, 0])
    # print(data[:, :, 1])
    # print(data[:, :, 2])
    data_rgb = data[:, :, : -1]
    # print(data_rgb)
    return data_rgb

#data_rgb = array2rgb("2_2.tif")
#print(data_rgb.shape)
#print(type(data_rgb))








