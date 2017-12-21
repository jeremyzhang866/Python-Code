#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 28_string_permutation.py
@Time: 2017/12/21 8:53
"""

"""
    给定一个字符串，输出其所有的排列，和数字基本是一样的
"""


def string_permutation_core(strs, p1, length):
    p2 = p1 + 1
    if p1 == length - 2:
        print(strs)
        strs[p1], strs[p2] = strs[p2], strs[p1]
        print(strs)
        strs[p1], strs[p2] = strs[p2], strs[p1]
        return

    string_permutation_core(strs, p1 + 1, length)
    while p2 < length:
        strs[p1], strs[p2] = strs[p2], strs[p1]
        string_permutation_core(strs, p1 + 1, length)
        strs[p1], strs[p2] = strs[p2], strs[p1]
        p2 += 1


def string_permutation(strs):
    p1 = 0
    length = len(strs)
    string_permutation_core(strs, p1, length)


if __name__ == '__main__':
    strs = ['1', '2', '3',"4"]
    string_permutation(strs)
