#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 36_reversed_oreder_num.py
@Time: 2017/11/25 12:36
Q:
    获得数组中的逆序对
"""


# 复杂度为n平方，过高，换方式
def solution_n_2(nums):
    count = 0
    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                count += 1
    return count


# 类似于归并排序的算法的思想，递归的去处理问题：



if __name__ == '__main__':
    nums = [7, 5, 6, 4]
    res = solution_n_2(nums)
    print(res)
