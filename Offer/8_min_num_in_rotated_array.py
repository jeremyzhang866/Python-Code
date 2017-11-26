#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 8_min_num_in_rotated_array.py
@Time: 2017/11/26 15:54
Q:
    旋转数组的最小数字。
"""


def min_num(numbers, length):

    # 特殊输入错误
    if numbers is None or length <= 0:
        raise Exception("抛出异常")

    index1, index2 = 0, length - 1

    # 用index1来初始化
    index_mid = index1

    while numbers[index1] >= numbers[index2]:
        if index2 - index1 == 1:
            index_mid = index2
            break

        # 获得中间的数据
        index_mid = (index2 + index1) // 2
        print(index_mid)
        if numbers[index_mid] >= numbers[index1]:
            index1 = index_mid
        # 没有else也是可以的。
        elif numbers[index_mid] <= numbers[index2]:
            index2 = index_mid

    return numbers[index_mid]


if __name__ == '__main__':
    test_list = [3, 4, 5, 1, 2]
    res = min_num(test_list, 5)
    print(res)
