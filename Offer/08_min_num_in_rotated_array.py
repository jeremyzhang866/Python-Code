#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 08_min_num_in_rotated_array.py
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

        if (numbers[index1] == numbers[index2]) and (numbers[index_mid] >= numbers[index1]):
            return min_in_order(numbers, index1, index2)

        if numbers[index_mid] >= numbers[index1]:
            index1 = index_mid
        # 没有else也是可以的。
        elif numbers[index_mid] <= numbers[index2]:
            index2 = index_mid

    return numbers[index_mid]


# 只是局部的一个顺序查找，而不是全部。这个思想很有点意思
def min_in_order(numbers, index1, index2):
    result = numbers[index1]
    index1 = index1 + 1
    # 循环的地方可以尽心基本运算
    while  index1 <= index2:
        if result > numbers[index1]:
            result = numbers[index1]
        index1 += 1
    return result



if __name__ == '__main__':
    test_list = [1, 1, 1, 0, 1]
    res = min_num(test_list, 5)
    print(res)
