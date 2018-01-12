# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：cv_demo
   Author :  zhangjinming
   Date：    2018/1/12
-------------------------------------------------
   Description:
    opencv
    基本操作
        1、存储与读取
        2、缩放，剪裁，补边
            resize
            img[:,:]
        3、色调，明暗，直方图，gamma曲线
            变换到hsv空间后，整个值都变换了
            hsv空间。色调(hue)，饱和度(saturation)，明度(value)  该空间直接调节避免考虑RBG空间的相关性。
                h的范围是0-180。其他两个为0-256

            色调：此空间，绿色值比黄色值要高
            饱和度：较低会使得图像变得更灰
            明度：使得图像变暗
            gamma 提升暗部细节，使之更加接近于0
                过于集中在0的话，会造成 丢失亮度细节；
                过于集中在256的话，会造成 丢失暗度度细节；



        4、仿射变换
        5、基本绘图
        6、视频功能
    数据增强
        1、随机剪裁
        2、随即旋转
        3、随即颜色和明暗
        4、多进程调和加速处理
    数据标注
        1、窗口循环
        2、鼠标和键盘事件
        3、物体检测



-------------------------------------------------
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse

# 生成一个矩阵
# img = np.array([
#     [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
#     [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
#     [[255, 255, 255], [128, 128, 128], [0, 0, 0]],
# ], dtype=np.uint8)

# 两种方法生成的图片略有不同
# plt.imsave("img_pyplot.jpg", img)
#
# cv2.imwrite('img_cv2.jpg', img)

#
# color_img = cv2.imread("tencent.png")
# print(color_img.shape)
#
# # 一般读取的就是单通道
# gray_img = cv2.imread("tencent.png", cv2.IMREAD_GRAYSCALE)
# print(gray_img.shape)
#
# # 存储的时候没有多通道这一说法
# cv2.imwrite('test_grayscale.jpg', gray_img)
# reload_grayscale = cv2.imread('test_grayscale.jpg')
# print(reload_grayscale.shape)


# 缩放，剪裁和补边操作
# img = cv2.imread("tencent.png")
# print(img.shape)
#
#
# img_abs = cv2.resize(img, (100, 200))
# print(img_abs.shape)
#
# img_rate = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
# print(img_rate.shape)
#
# # 剪裁图片
# patch_tencent = img[200:300, 500:600]
# cv2.imwrite("patch_tencent.jpg", patch_tencent)

# 调节在HSV空间操作
img = cv2.imread("fruit.jpeg")
# 变换到HSV空间   COLOR_BGR2HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

turn_green_hsv = img_hsv.copy()

# 调整色度，使得其变得更加绿色
turn_green_hsv[:, :, 0] = (turn_green_hsv[:, :, 0] + 35) % 180

# 要把空间转换过来
turn_green_img = cv2.cvtColor(turn_green_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite("turn_green_img.jpg", turn_green_img)

color_less_hsv = img_hsv.copy()
color_less_hsv[:, :, 1] = 0.8 * color_less_hsv[:, :, 1]
color_less_hsv_img = cv2.cvtColor(color_less_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite("color_less_hsv.jpg", color_less_hsv)

darker_hsv = img_hsv.copy()
darker_hsv[:, :, 2] = 0.5 * darker_hsv[:, :, 2]
darker_img = cv2.cvtColor(darker_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite("darker_img.jpg", darker_img)



