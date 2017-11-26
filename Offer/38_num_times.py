#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 38_num_times.py
@Time: 2017/11/25 13:09
Q:
    数字在排序数组中出现的次数
"""
# 充分利用排序和二分查找的思路，一下子找到相等元素的最左边和最右边，返回值
# 当不重复的时候，输出索引


def sol_binary_search(nums, key, count):

    # 要注意索引和值的问题:
    if len(nums) <= 2:
        for i, val in enumerate(nums):
            if val == key:
                return count + i
        else:
            return False
    print(nums)
    middle_value = nums[len(nums) // 2]
    if key < middle_value:
        return sol_binary_search(nums[:len(nums) // 2], key, count)
    elif key > middle_value:
        count = count + len(nums) // 2
        return sol_binary_search(nums[len(nums) // 2:], key, count)
    else:
        return count + len(nums) // 2


def get_first_k(numbers, length, k, start, end):

    # 当函数本身返回的是索引的时候，这里return的是-1。
    # 而且总是在最上面判断特殊输入测试。
    if start > end:
        return -1

    mid_index = (start + end) // 2
    mid_val = numbers[mid_index]

    if mid_val == k:
        if (mid_index > 0 and numbers[mid_index - 1] != k) or mid_index == 0:
            return mid_index
        else:
            end = mid_index - 1
    elif mid_val > k:
        end = mid_index - 1
    else:
        start = mid_index + 1

    # 注意到这里的递归。前面三项都是不变得，变得始终只是start, 和 end 的结果。
    return get_first_k(numbers, length, k, start, end)

# def get_last_k(numbers, length, k, start, end):
#     if start > end:
#         return -1
#
#     mid_index = (start + end) // 2
#     mid_val = numbers[mid_index]
#
#     if mid_val == k:
#         if (mi)



if __name__ == '__main__':
    nums = [1, 3, 5, 5, 5,  7, 8, 9, 15, 15, 22, 31, 31, 31, 45, 88]
    length = len(nums)
    k = 15
    start = 0
    end = length - 1
    res = get_first_k(nums, length, k, start, end)
    print(res)
