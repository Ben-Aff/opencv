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


if __name__=='__main__':
    color_space_demo()