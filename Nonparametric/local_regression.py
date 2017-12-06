#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: local_regression.py
@Time: 2017/12/6 15:09
"""
import csv
import matplotlib.pyplot as plt


def get_set(n):
    # 从数据库中，导入数据
    csv_reader = csv.reader(open("CMB_data.csv", encoding="utf-8"))
    power = [row[1] for row in csv_reader]
    return [float(x) for x in power[:n]]


def kernel_function(x):
    # the  boxcar kernel
    if abs(x) <= 1:
        return 0.5
    else:
        return 0


def l_func(n, h, x, i):
    # 生成n个数字
    xs = list(range(n))
    denominator = 0
    for j in range(n):
        denominator += kernel_function((x - xs[j]) / h)
    return kernel_function((x - xs[i] - 1) / h)/denominator


def liner_smoother(n, h, x):
    # 线性平滑的函数
    # 得到每一个x的平滑值
    ys = get_set(n)
    sum = 0
    for i in range(n):
        sum += l_func(n, h, x, i)*ys[i]
    return sum


def out(n, h):
    # 输出线性平滑的结果
    # 并画出图像
    out_data = []
    for x in range(n):
        out_data.append(liner_smoother(n, h, x))
    return out_data


def out_plt(n, h):
    # out_data = out(n, h)
    out_data = get_set(n)
    plt.scatter(range(n), out_data, marker=".")
    # plt.plot(out_data)
    plt.xlabel("Multiple")
    plt.ylabel("Power")
    # plt.title("h = %d" %h)
    plt.title("n = %d" %n)
    plt.show()


if __name__ == '__main__':
    # 数据量选择
    n = 800
    # 带宽选择
    h = 50
    out_plt(n, h)
