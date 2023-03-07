import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#图像像素的乘除算术操作(整个图片的像素值乘除某一倍数-提高了图片的对比度)
def math2_demo():
    image=cv.imread('E:/8.opnecv4/opencv/images/test.png')
    cv.imshow('input',image)
    h,w,c=image.shape
    black=np.zeros((h,w,c),dtype=np.uint8)
    black[:,:]=(2,2,2)
    cv.imshow('black',black)
    result1=cv.multiply(image,black)#加像素值，增加图片的亮度
    result2=cv.divide(image,black)#减像素值，减少图片的亮度
    cv.imshow('result1',result1)
    cv.imshow('result2',result2)
    cv.waitKey(0)
    cv.destroyAllWindows()
if __name__=='__main__':
    math2_demo()