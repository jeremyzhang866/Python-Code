#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 03_find_in_partially_sorted_martix.py
@Time: 2017/12/21 11:23
"""
"""
    找出是否含有某元素。P38.
    充分利用排序的信息，于是从左下角或者右下角。
"""
import numpy as np


def find_in_partially_sorted_matrix(nums, number):
    # 获取坐标
    x, y = 0, 3
    # 不同时怼到左下角
    while (x != 4) or (y != -1):
        if nums[x][y] == number:
            return True
        elif nums[x][y] > number:
            y = y - 1
        else:
            x = x + 1
    return False


if __name__ == '__main__':
    nums = np.arange(1, 17).reshape(4, 4)
    number = 17
    res = find_in_partially_sorted_matrix(nums, number)
    print(res)
