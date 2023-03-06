import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#图片的读取加载与展示
def read_demo():
    image=cv.imread('D:/project/Opencv/study2/images/test.png')
    cv.imshow('input test image-LINNA',image)
    cv.waitKey(0)
    cv.destroyAllWindows
#图片的色彩
def color_space_demo():
    image=cv.imread

