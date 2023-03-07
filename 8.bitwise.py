import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#opencv中图像像素的逻辑操作
def bitwise_demo():
    image = cv.imread('E:/8.opnecv4/opencv/images/test.png')
    b1=np.zeros((400,400,3),dtype=np.uint8)
    b1[:,:]=(255,0,255)#蓝色混合红色
    b2=np.zeros((400,400,3),dtype=np.uint8)
    b2[:,:]=(0,255,0)#绿色
    dst1=cv.bitwise_and(b1,b2)#将图像b1与图像b2进行与操作(0,0,0)-全白
    dst2=cv.bitwise_or(b1,b2)#将图像b1与图像b2进行或操作（255，255，255）-全黑
    cv.imshow('b1',b1)
    cv.imshow('b2',b2)
    cv.imshow('bitwise_and',dst1)
    cv.imshow('bitwise_or',dst2)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__=='__main__':
    bitwise_demo()