import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#opencv中图片的色彩空间转换
def color_space_demo():
    image=cv.imread('E:/8.opnecv4/opencv/images/test.png')
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)#BGR TO GRAY
    hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)#BGR TO HSV
    cv.imshow('GRAY', gray)
    cv.imshow('HSV', hsv)
    cv.waitKey(0)
    cv.destroyAllWindows()

#opencv中图像色彩空间转换
def color_space_demo():
    b1=cv.imread('E:/8.opnecv4/opencv/images/greenback.png')
    print(b1.shape)
    cv.imshow('input',b1)#展示原图像
    hsv=cv.cvtColor(b1,cv.COLOR_BGR2HSV)
    cv.imshow('hsv',hsv)#将原图像转换为hsv的形式
    mask=cv.inRange(hsv,(35,43,36),(77,255,255))
    cv.bitwise_not(mask,mask)
    result=cv.bitwise_and(b1,b1,mask=mask)
    cv.imshow('mask',hsv)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__=='__main__':
    color_space_demo()