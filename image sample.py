import cv2
import numpy as np
import matplotlib.pyplot as plt
def image_sample():
#读取原始图像
    img = cv2.imread('E:/8.opnecv4/opencv/images/test.png')
#获取图像高度和宽度
    height=img.shape[0]
    width=img.shape[1]
#采样转换成16*16区域
    numHeight=int(height/16)
    numWidth =int(width/16)
#创建空白图像
    empty_img=np.zeros((height, width,3),np.uint8)
#图像循环采样16*16区域
    for i in range(16):
#获取Y坐标
        y = i * numHeight
        for j in range(16):
#获取X坐标
            x = j * numWidth
#获取填充颜色 左上角像素点
            b = img[y, x][0]
            g = img[y, x][1]
            r = img[y, x][2]
            # 循环设置小区域采样
            for n in range(numHeight):
                for m in range(numWidth):
                    new_img[y + n, x + m][0] = np.uint8(b)
                    new_img[y + n, x + m][1] = np.uint8(g)
                    new_img[y + n, x + m][2] = np.uint8(r)

    # 显示图像
    cv2.imshow("src", img)
    cv2.imshow("Sampling", new_img)

    # 等待显示
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    image_sample()