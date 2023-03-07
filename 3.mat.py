import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#opencv中图像对象的创建与赋值
#opencv中创建空白图像
def mat_demo():
    image=cv.imread('E:/8.opnecv4/opencv/images/test.png')
    print(image.shape)#HWC
    h,w,c=image.shape
    black=np.zeros((h,w,c),dtype=np.uint8)#opencv中创建空白图像
    cv.imshow('black',black)
    cv.imshow('image',image)
    cv.waitKey(0)
    cv.destroyAllWindows()
#opencv中局部区域的显示
def mat_demo2():
    image=cv.imread('E:/8.opnecv4/opencv/images/test.png')
    h,w,c=image.shape
    roi=image[100:280,60:280,:]
    black=np.zeros((h,w,c),dtype=np.uint8)#opencv中创建空白图像
    black[100:280,60:280,:]=roi
    cv.imshow('black',black)
    cv.imshow('image',image)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__=='__main__':
    mat_demo()
    mat_demo2()