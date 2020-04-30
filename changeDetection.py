# -*- coding: utf-8 -*-

# Author: chenxiaoping
# Time:   2018/12/18
# Name:   Tif2array

import os
import cv2

from Tif_to_array import array2rgb
from anomalyDetection import plot, read_image, save_saliency_image, get_img_name

def save_image(saliency_image, img_name):
    save_dir = ".temp/"
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    filename = save_dir + "%s.jpg" % img_name
    cv2.imwrite(filename, saliency_image)
    return filename

#二值化
def binarization(saliency_image):
     retval, im_at_fixed = cv2.threshold(saliency_image, 3, 255, cv2.THRESH_BINARY)
     return im_at_fixed

#读入两张图片，输出图片
def changeDetection(file1, file2, savename):
    data_rgb1 = array2rgb(file1)
    data_rgb2 = array2rgb(file2)
    image_gray1 = read_image(data_rgb1)
    image_gray2 = read_image(data_rgb2)
    image_gray1 = image_gray1[0:900,0:450]
    image_gray2 = image_gray2[0:900,0:450]   
    image_gray3 = image_gray1-image_gray2
    
    
    plot(image_gray1)
    plot(image_gray2)
    bin_image = binarization(image_gray3)
    image_name = get_img_name(savename)
    filename = save_image(bin_image, image_name)
    return filename
    #显示图片
    #plot(image_gray3)
    
      


#if __name__=="__main__":
 #  changeDetection("C:/Users/lenovo'/Desktop/20190410202011.png","C:/Users/lenovo'/Desktop/20190410202011.png",".result2.jpg")
    
    