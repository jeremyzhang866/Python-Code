#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 55_first_char_in_stream.py
@Time: 2017/12/27 21:16
"""
"""
找出数据流中第一次只出现的char
"""


def first_char_in_stream(strings):
    occurrence = [-1 for _ in range(256)] + [len(strings) + 1]
    # 遍历的插入一边，且将出现的顺序标个号码，index从1开始算起
    index = 1
    for string in strings:
        if occurrence[ord(string)] == -1:
            occurrence[ord(string)] = index
            index += 1
        elif occurrence[ord(string)] > 0:
            occurrence[ord(string)] = -2

    # 遍历查找出index指标最小的整数
    min_index = 256
    for i in range(256):
        if occurrence[i] > 0:
            min_index = i if occurrence[i] < occurrence[min_index] else min_index
    if min_index >= 256:
        return "没有重复的元素"
    return chr(min_index)


def main():
    strings = "googel"
    res = first_char_in_stream(strings)
    print(res)


def fake():
    strings = "google"
    for string in strings:
        print(ord(string))


if __name__ == '__main__':
    main()
