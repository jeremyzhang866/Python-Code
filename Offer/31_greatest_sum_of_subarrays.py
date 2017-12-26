#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 31_greatest_sum_of_subarrays.py
@Time: 2017/12/25 16:29
"""
"""
    连续子数组的最大和
"""


def dir_sol(nums):
    length = len(nums)
    sol = 0
    for i in range(length):
        j = i
        while j <= length:
            temp_sum = sum(nums[i:j])
            sol = temp_sum if temp_sum > sol else sol
            j += 1
    return sol


def dp_sol(nums):
    """
    更抽象用动态规划的思想；
    一次遍历即可获得结果。
    :param nums:
    :return:
    """
    res = 0
    pre_item = nums[0]
    for i in range(1, len(nums)):
        after_item = pre_item + nums[i] if pre_item > 0 else nums[i]
        res = after_item if after_item >= res else res
        print(res, end=" ")
        pre_item = after_item
    return res


def divide(nums):
    return ""


def main():
    nums = [-3, 1, -2, 3, 10, -4, 7, 2, -5]
    res_dir = dir_sol(nums)
    res_dp = dp_sol(nums)
    res_divide = divide(nums)
    print(res_dir)
    print(res_dp)
    print(res_divide)


if __name__ == '__main__':
    main()
