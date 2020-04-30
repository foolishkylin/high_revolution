import cv2
import  numpy as np
import scipy.misc
from scipy.misc import imsave
path = "C:/Users/lenovo'/Desktop/cut/trainset/"


for n in range(1):  #可根据文件夹rename后的图片数量更改range中的数字
    img = scipy.misc.imread(path+str(n+1)+".PNG").astype(np.float)
    # img=imread(path+str(n+1)+".PNG")
    print(img.shape[0],img.shape[1])
    xstart = int((img.shape[0]-500)//2)
    ystart = int((img.shape[1]-500)//2)
    cropImg = img[xstart:xstart+500, ystart:ystart+500]  #裁剪
    # img=scipy.misc.imresize(img,(500, 500))
    #缩放
    # img.shape[0]=500
    # img.shape[1]=500
    imsave(path+"test2.png",cropImg)


# path = "C:/Users/lenovo'/Desktop/cut/trainset/1.PNG"
# def resize_img_keep_ratio(img_name,target_size):
#     img = cv2.imread(img_name)
#     old_size= img.shape[0:2]
#     #ratio = min(float(target_size)/(old_size))
#     ratio = min(float(target_size[i])/(old_size[i]) for i in range(len(old_size)))
#     new_size = tuple([int(i*ratio) for i in old_size])
#     img = cv2.resize(img,(new_size[1], new_size[0]))
#     pad_w = target_size[1] - new_size[1]
#     pad_h = target_size[0] - new_size[0]
#     top,bottom = pad_h//2, pad_h-(pad_h//2)
#     left,right = pad_w//2, pad_w -(pad_w//2)
#     img_new = cv2.copyMakeBorder(img,top,bottom,left,right,cv2.BORDER_CONSTANT,None,(0,0,0))
#     cv2.imwrite(path+"change",img_new)
# if __name__ == '__main__':
#     target_size=[500,500]
#     resize_img_keep_ratio(path,target_size)