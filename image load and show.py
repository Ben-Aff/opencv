import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#图片的读取加载与展示
def read_demo():
    image=cv.imread('E:/8.opnecv4/opencv/images/test.png')
    cv.imshow('input test image-LINNA',image)
    cv.waitKey(0)
    cv.destroyAllWindows
#图片的色彩空间转换
def color_space_demo():
    image=cv.imread('E:/8.opnecv4/opencv/images/test.png')
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)#BGR TO GRAY
    hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)#BGR TO HSV
    cv.imshow('GRAY', gray)
    cv.imshow('HSV', hsv)
    cv.waitKey(0)
    cv.destroyAllWindows
'''图像对象的创建与赋值'''
#opencv中创建空白图像
def mat_demo():
    image=cv.imread('E:/8.opnecv4/opencv/images/test.png')
    print(image.shape)#HWC
    hwc=image.shape
    black=np.zeros((hwc),dtype=np.uint8)#opencv中创建空白图像
    cv.imshow('black',black)
    cv.imshow('image',image)
    cv.waitKey(0)
    cv.destroyAllWindows()
#opencv中局部区域的显示
def mat_demo2():
    image=cv.imread('E:/8.opnecv4/opencv/images/test.png')
    hwc=image.shape
    roi=image[100:280,60:280,:]
    black=np.zeros((hwc),dtype=np.uint8)#opencv中创建空白图像
    black[100:280,60:280,:]=roi
    cv.imshow('black',black)
    cv.imshow('image',image)
    cv.waitKey(0)
    cv.destroyAllWindows()
#opencv中图像的拷贝的两种方式
def mat_demo3():
    image=cv.imread('E:/8.opnecv4/opencv/images/test.png')
    black1=np.copy(image)
    black2=image
    cv.imshow('black1',black1)
    cv.imshow('black2',black2)
    cv.waitKey(0)
    cv.destroyAllWindows()
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
#图像的保存
    cv.imwrite('E:/8.opnecv4/opencv/images/picture after changing.png',image)
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
    cv.destroyAllWindows(0)
#opencv中的键盘相应操作
def key_demo():
    pass




#opencv中的自带颜色表操作
def color_table_demo():
    colormap=[
      cv.COLORMAP_AUTUMN,
      cv.COLORMAP_BONE,
      cv.COLORMAP_JET,
      cv.COLORMAP_WINTER,
      cv.COLORMAP_RAINBOW,
      cv.COLORMAP_OCEAN,
      cv.COLORMAP_SUMMER,
      cv.COLORMAP_SPRING,
      cv.COLORMAP_COOL,
      cv.COLORMAP_PINK,
      cv.COLORMAP_HOT,
      cv.COLORMAP_PARULA,
      cv.COLORMAP_MAGMA,
      cv.COLORMAP_INFERNO,
      cv.COLORMAP_PLASMA,
      cv.COLORMAP_VIRIDIS,
      cv.COLORMAP_CIVIDIS,
      cv.COLORMAP_TWILIGHT,
      cv.COLORMAP_TWILIGHT_SHIFTED]
    image = cv.imread('E:/8.opnecv4/opencv/images/test.png')
    cv.namedWindow('input',cv.WINDOW_AUTOSIZE)
    cv.imshow('input', image)
    index=0
    while True:
        c=cv.waitKey(500)
        dst=cv.applyColorMap(image,colormap[index%19])#一共有19个风格
        index+=1
        cv.imshow('color style',dst)
        if c==27:
            break
    cv.destroyAllWindows()


if __name__=='__main__':
    color_table_demo()