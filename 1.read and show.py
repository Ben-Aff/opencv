#图像的读取与加载
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
def read_demo():
    image=cv.imread('E:/8.opnecv4/opencv/images/test.png')
    cv.imshow('input test image',image)
    cv.waitKey(0)
    cv.destroyAllWindows()



if __name__=='__main__':
    read_demo()