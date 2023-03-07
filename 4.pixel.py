import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#图像像素的写操作
def pixel_demo():
    image=cv.imread('E:/8.opnecv4/opencv/images/test.png')
    h,w,c=image.shape
    cv.imshow('picture before changing',image)
    for row in range(h):
        for col in range(w):
            b,g,r=image[row,col]
            image[row,col]=(255-b,255-g,255-r)
    cv.imshow('picture after changing',image)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__=='__main__':
    pixel_demo()