#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com
@File: 44_continous_cards.py
@Time: 2017/12/9 17:00
"""
"""
    所谓抽象建模能力，这里体现在如何去思考问题
    扑克牌问题，不重复抽样
"""
import random


def is_order(n):
    # 扑克牌数组
    nums = [0, 0] + list(range(1, 14))
    # 待测序列
    seq = list(random.sample(nums, n))
    seq.sort()
    print(seq)
    zero_count = 0
    i = 0
    distance = 0
    while i < n - 1:
        if seq[i] == 0:
            zero_count += 1
        else:
            distance += abs(seq[i + 1] - seq[i] - 1)
        i += 1

    if zero_count >= distance:
        return True
    else:
        return False


if __name__ == '__main__':
    n = 3
    result = is_order(n)
    print(result)
