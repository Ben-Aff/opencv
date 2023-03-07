import cv2 as cv
import numpy as np

def quantization_processing():
#读取加载原图像
    test1=cv.imread('E:/8.opnecv4/opencv/images/test1.png',1)
    cv.imshow('input picture',test1)
#创建空白图像
    h,w,c=test1.shape
    empty_picture=np.zeros((h,w,c))
#遍历原始图像中的每一个像素点
    for height in range(h):
        for weight in range(w):
            for channel in range(c):
                    if test1[height,weight][channel]<128:
                        gray=0
                    else:
                        gray=128
                    empty_picture[height,weight][channel]=np.uint8(gray)
    cv.imshow('picture after twice quantization processing',empty_picture)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__=='__main__':
    quantization_processing()