#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 51_duplication_in_array.py
@Time: 2017/12/27 13:08
"""
"""
    数组中重复的数字
"""


def duplication_in_array_direct(nums):
    """
    空间复杂度也为O(n)
    :param nums:
    :return:
    """
    length = len(nums)
    lst = [0 for i in range(length)]
    for num in nums:
        lst[num] += 1
    res = []
    for i, ls in enumerate(lst):
        if ls > 1:
           res.append(i)
    return res


def duplication_in_array(nums):
    """
    TC:O(n)
    SC:O(1) 仅在自己这个数组上操作
    :param nums:
    :return:返回布尔值。是否存在重复的数字
    """
    length = len(nums)
    for i in range(length):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return True
            # 此时需要这样的方式进行调整顺序
            temp = nums[nums[i]]
            nums[nums[i]] = nums[i]
            nums[i] = temp
    return False


def main():
    nums = [2, 3, 1, 0, 1]
    res = duplication_in_array(nums)
    print(res)


def fake():
    nums = [2, 3, 1, 0]
    res = duplication_in_array_direct(nums)
    print(res)


if __name__ == '__main__':
    main()
    # fake()
