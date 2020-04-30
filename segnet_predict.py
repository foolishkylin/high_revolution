import cv2
import random
import numpy as np
import os
import argparse
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
import PIL
import keras
keras.backend.clear_session()

os.environ["CUDA_VISIBLE_DEVICES"] = "1"

TEST_SET = ['1.png']

image_size = 256

classes = [0. ,  1.,  2.,   3.  , 4.]  
  
labelencoder = LabelEncoder()  
labelencoder.fit(classes) 

# def args_parse():
# # construct the argument parse and parse the arguments
#     ap = argparse.ArgumentParser()
#     ap.add_argument("-m", "--model", required=True,
#         help="path to trained model model")
#     ap.add_argument("-s", "--stride", required=False,
#         help="crop slide stride", type=int, default=image_size)
#     args = vars(ap.parse_args())
#     return args

    
def predict(arg):
    # load the trained convolutional neural network
    print("[INFO] loading network...")
    # model = load_model(args["model"])

    model = load_model('segnet.h5')
    print("loading done")
    # stride = args['stride']
    stride = 256
    print(arg)
    #load the image
    print("loading picture...")
    image = cv2.imread(arg)
    print('loading done')
    h,w,_ = image.shape
    padding_h = (h//stride + 1) * stride
    padding_w = (w//stride + 1) * stride
    padding_img = np.zeros((padding_h,padding_w,3),dtype=np.uint8)
    padding_img[0:h,0:w,:] = image[:,:,:]
    padding_img = padding_img.astype("float") / 255.0
    padding_img = img_to_array(padding_img)
    print('src:',padding_img.shape)
    mask_whole = np.zeros((padding_h,padding_w),dtype=np.uint8)
    for i in range(padding_h//stride):
        for j in range(padding_w//stride):
            crop = padding_img[i*stride:i*stride+image_size,j*stride:j*stride+image_size,:3]
            ch,cw,_ = crop.shape
            if ch != 256 or cw != 256:
                print('invalid size!')
                continue
                    
            crop = np.expand_dims(crop, axis=0)
            #print 'crop:',crop.shape
            pred = model.predict_classes(crop,verbose=2)
            pred = labelencoder.inverse_transform(pred[0])
            #print (np.unique(pred))
            pred = pred.reshape((256,256)).astype(np.uint8)
            #print 'pred:',pred.shape
            mask_whole[i*stride:i*stride+image_size,j*stride:j*stride+image_size] = pred[:,:]

    mask_whole[0:h, 0:w] = mask_whole[0:h, 0:w] * 150
    # there are ez to make error
    cv2.imwrite('pre.png',mask_whole[0:h,0:w])
    img = PIL.Image.open('pre.png')
    width = img.size[0]
    height = img.size[1]
    im = img.convert('RGB')
    print("painting")
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            if r == 150 or r == 151:
                im.putpixel((x, y), (159, 255, 84))
            if 192 <= r <= 196:
                im.putpixel((x, y), (0, 255, 255))
            if 40 <= r <= 66:
                im.putpixel((x, y), (255, 191, 0))
    im.save("change.png")
    path = 'change.png'
    return path
# if __name__ == '__main__':
#     args = args_parse()
#     predict(args)
#
#

