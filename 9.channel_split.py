import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#opencv中通道的分离与合并
def channel_split():
#使用python中的切片操作进行通道的分离与合并
    b1=cv.imread('E:/8.opnecv4/opencv/images/yuan_test.png')
    cv.imshow('input',b1)
    cv.imshow('b1',b1[:,:,2])
    mv=cv.split(b1)
    print(mv)
    mv[0][:,:]=255
    result=cv.merge(mv)
    cv.imshow('result',result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__=='__main__':
    channel_split()