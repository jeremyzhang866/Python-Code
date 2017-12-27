#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 41_two_numbers_with_sum.py
@Time: 2017/12/26 20:26
"""
"""
    从递增数组中寻找出两个和为s的 数字。存在多对，输出所有的数字对。不考虑重复元素
"""


def sol(nums, res_ls, S):
    """
    从递增数组中寻找出两个和为s的 数字。存在多对，输出所有的数字对。不考虑重复元素
    :param nums:
    :param res_ls: 结果数组
    :param S: 要寻找到的值
    :return:
    """
    length = len(nums)
    p1 = 0
    p2 = length - 1
    while p1 != p2:
        if nums[p1] + nums[p2] > S:
            p2 -= 1
        elif nums[p1] + nums[p2] < S:
            p1 += 1
        else:
            res_ls.append([nums[p1], nums[p2]])
            p2 -= 1
            p1 += 1


def continues_seq_with_sum(nums, res_ls, S):
    p1 = 0
    p2 = 1
    while nums[p1] < (S + 1)//2:
        print(sum(nums[p1:p2 + 1]))
        if sum(nums[p1:p2 + 1]) < S:
            p2 += 1
        elif sum(nums[p1:p2 + 1]) > S:
            p1 += 1
        else:
            res_ls.append(nums[p1: p2 + 1])
            p2 += 1
    if not len(res_ls):
        return "没有找到这样的数组"
    return res_ls


def main():
    nums1 = [1, 2, 4, 7, 11, 15]
    res_ls1 = []
    S1 = 15
    sol(nums1, res_ls1, S1)
    # print(res_ls1)

    nums2 = list(range(1, 9))
    res_ls2 = []
    S2 = 9
    a = continues_seq_with_sum(nums2, res_ls2, S2)
    print(a)


if __name__ == '__main__':
    main()
