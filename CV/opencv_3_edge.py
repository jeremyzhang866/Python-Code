# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：opencv_3_edge.py
   Author :  zhangjinming
   Date：    2018/1/13
-------------------------------------------------
   Description:
-------------------------------------------------
"""
import cv2
import numpy

def stroke_edge(src, dst, blur_ksize=7, edge_ksize=5):
    # 大于等于3，才进行模糊处理
    if blur_ksize >= 3:
        blurred_img = cv2.medianBlur(src, blur_ksize)
        gray_img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    else:
        gray_img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    cv2.Laplacian(gray_img, cv2.CV_8U, gray_img, ksize=edge_ksize)

    # cv2.imshow("gray_img", gray_img)
    # cv2.waitKey()

    normalized_inverse_alpha = (1.0 / 255)*(255 - gray_img)
    channels = cv2.split(src)
    for channel in channels:
        channel[:] = channel * normalized_inverse_alpha

    cv2.merge(channels, dst)
    cv2.imshow("dst_img", dst)
    cv2.waitKey()


def demo_canny(src):
    cv2.imwrite("canny_fruit.jpg", cv2.Canny(src, 200, 300))
    cv2.imshow("canny", cv2.imread("canny_fruit.jpg"))
    cv2.waitKey()


if __name__ == '__main__':
    src = cv2.imread("fruit1.jpeg", 0)
    # dst = cv2.imread("fruit1.jpeg")
    # stroke_edge(src, dst, 7, 5)
    demo_canny(src)
