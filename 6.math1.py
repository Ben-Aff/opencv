import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#图像像素的加减算术操作(增加/减少图片的像素值来使图片变亮/暗)
def math1_demo():
    image=cv.imread('E:/8.opnecv4/opencv/images/test.png')
    cv.imshow('input',image)
    h,w,c=image.shape
    black=np.zeros((h,w,c),dtype=np.uint8)
    black[:,:]=(80,80,80)
    cv.imshow('black',black)
    result1=cv.add(image,black)#加像素值，增加图片的亮度
    result2=cv.subtract(image,black)#减像素值，减少图片的亮度
    cv.imshow('result1',result1)
    cv.imshow('result2',result2)
    cv.waitKey(0)
    cv.destroyAllWindows(0)

if __name__=='__main__':
    math1_demo()