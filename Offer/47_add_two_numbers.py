#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 47_add_two_numbers.py
@Time: 2017/12/21 10:16
"""
"""
    计算和，不用加减乘除
    思路：很明显就是位运算问题  
"""


# def get_bin_num(x):
#     strs = ""
#     while x % 2 != 0:
#         strs =


def add_two_numbers(x, y):
    # 下面代码其实是 “加法” 的一个抽象
    res1 = x ^ y
    res2 = (x & y) << 1
    return res1 + res2


def add_two_numbers_iter(x, y):
    sum_, carry = 0, 0
    while y != 0:
        sum_ = x ^ y
        # 注：下面的结果很可能为0
        carry = (x & y) << 1
        x = sum_
        y = carry
    return sum_


def add_two_numbers_recu(x, y):
    if y == 0:
        return x
    res1 = x ^ y
    res2 = (x & y) << 1
    return add_two_numbers_recu(res1, res2)

if __name__ == '__main__':
    x = 50
    y = 17
    res = add_two_numbers_recu(x, y)
    print(res)
