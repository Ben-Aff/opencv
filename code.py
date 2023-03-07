import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#opencv中图像色彩空间转换
def color_space_demo():
    b1=cv.imread('E:/8.opnecv4/opencv/images/greenback.png')
    print(b1.shape)
    cv.imshow('input',b1)
    cv.waitKey(0)
    cv.destroyAllWindows()
    hsv=cv.cvtColor(b1,cv.COLOR_BGR2HSV)
    cv.imshow('hsv',hsv)
    mask=cv.inRange(hsv,(35,43,36),(77,255,255))
    cv.bitwise_not(mask,mask)
    result=cv.bitwise_and(b1,b1,mask=mask)
    cv.imshow('mask',hsv)
    cv.waitKey(0)
    cv.destroyAllWindows()
#opencv中像素值统计
def pixel_sta():
    b1=cv.imread('E:/8.opnecv4/opencv/images/ttt.png')
    print(b1.shape)
    cv.imshow('input',b1)
    means,dev=cv.meanStdDev(b1)
    print(means,dev)
    cv.waitKey(0)
    cv.destroyAllWindows()
    b2=np.zeros((512,512,3),dtype=np.uint8)
    print(b1.shape)
    means,dev=cv.meanStdDev(b2)
    print(means,dev)
    b3=np.zeros((512,512,3),dtype=np.uint8)
    print(np.min(b1[:,:,-1]))#统计通道的最小值
    print(np.max(b1[:,:,-1]))#统计通道的最大值








if __name__=='__main__':
    pixel_sta()
