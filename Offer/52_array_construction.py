#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 52_array_construction.py
@Time: 2017/12/27 13:07
"""
"""
    构造乘积矩阵
"""


def sol_direct(nums):
    """
    简单算法
    :param nums:
    :return:
    """
    length = len(nums)
    mul = 1
    for i in range(length):
        mul *= nums[i]
    res = []
    for i in range(length):
        res.append(mul // nums[i])
    return res


def array_construction(nums):
    """
    一次遍历，充分的保存求得的信息
    :param nums:
    :return:
    """
    length = len(nums)
    cls = [1 for _ in range(length)]
    dls = [1 for _ in range(length)]
    i = 1
    while i <= length - 1:
        cls[i] = cls[i - 1] * nums[i - 1]
        dls[length - 1- i] = dls[length - i] * nums[length - i]
        i += 1
    res = []
    for i in range(length):
        res.append(cls[i] * dls[i])
    return res


def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    res = sol_direct(nums)
    res1 = array_construction(nums)
    print(res)
    print(res1)





if __name__ == '__main__':
    main()
