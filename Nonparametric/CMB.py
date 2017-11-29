#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: CMB.py
@Time: 2017/11/29 12:09
"""

import csv
import matplotlib.pyplot as plt


def plt_scatter(k):
    csv_reader = csv.reader(open("CMB_data.csv", encoding="utf-8"))
    power = [row[1] for row in csv_reader]

    # 绘图范围
    plt_list = power[:k]
    plt_len = len(plt_list)

    # plt画图
    plt.scatter(range(plt_len), plt_list,marker=".")
    plt.xlabel("Multiple")
    plt.ylabel("Power")

    plt.show()


if __name__ == '__main__':
    k = 400
    plt_scatter(k)
