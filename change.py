# from PIL import Image
# import os
# src = cv2.imread("D:/Satellite-Segmentation-master/Satellite-Segmentation-master/unet/unet_train_set/label/0.png");
# H,W = src.shape
# for h in H:
#     for w in W:
#         if
# for i in  src.rows:
#     p_src = src.ptr(i)
#     for j in src.cols:
#         if p_src[j] == WATER:
#             p_src[j] = BUILDING
#         elif p_src[j] == ROAD:
#             p_src[j] = WATER
#         elif p_src[j] == BUILDING:
#             p_src[j] = ROAD
# cv2.imwrite("proc5.png", src)


# i = 1
# j = 1
# img = Image.open("D:/Satellite-Segmentation-master/Satellite-Segmentation-master/unet/predict/pre1.png")#读取系统的内照片
# print (img.size)#打印图片大小
# print (img.getpixel((4,4)))
# width = img.size[0]#长度
# height = img.size[1]#宽度
# for i in range(0,width):#遍历所有长度的点
#     for j in range(0,height):#遍历所有宽度的点
#         data = (img.getpixel((i,j)))#打印该图片的所有点
#         print (data)#打印每个像素点的颜色RGBA的值(r,g,b,alpha)
#         print (data[0])#打印RGBA的r值
#         if (data[0]>=170 and data[1]>=170 and data[2]>=170):
#             img.putpixel((i,j),(234,53,57,255))
# img = img.convert("RGB")#把图片强制转成RGB
# img.save("D:/Satellite-Segmentation-master/Satellite-Segmentation-master/unet/predict/pre1.png")#保存修改像素点后的图片


import skimage.io as io
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
# image='D:/Satellite-Segmentation-master/Satellite-Segmentation-master/unet/predict/pre1.png'
# img=Image.open(np.str(image)).convert('L')
# img=np.array(img)
TEST_SET = ['pre1.png','pre2.png','pre3.png']
for n in range(len(TEST_SET)):
        path = TEST_SET[n]
        img=Image.open("D:/Satellite-Segmentation-master/Satellite-Segmentation-master/segnet/predict/"+path)
        width = img.size[0]
        height = img.size[1]
        im = img.convert('RGB')
        print("picture"+str((n+1)))
        for x in range(width):
                for y in range(height):
                        r, g, b = im.getpixel((x,y))
                        rgb = (r, g, b)
                        if r==150 or r==151:
                                im.putpixel((x,y),(159,255,84))
                        if r>=192 and r<=196:
                                im.putpixel((x, y), (0, 255, 255))
                        if r>=40 and r<=66:
                                im.putpixel((x, y), (255, 191, 0))

        im.save("D:/Satellite-Segmentation-master/Satellite-Segmentation-master/segnet/predict/change"+str((n+1))+".png")
# H,W = img.shape
# for i in H:
#         for j in W:
#                 if img[i,j]==ROAD:
#                         img[i,j]=255
#                 if img[i,j]==BUILDING:
#                         img[i,j]=128
#
# image.show(img)

# plt.figure("black-white")
# plt.imshow(img)
# plt.show()
