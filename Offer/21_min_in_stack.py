#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com
@File: 21_min_in_stack.py
@Time: 2017/12/7 16:21
"""
'''
包含min函数的栈——时刻获得该栈的最小值
用辅助栈去思考问题,为什么要辅助栈？
因为:当目前的最小元素被弹出后，就解决不了问题了。如果只用成员变量的话，会被更新。这个最小值应当是一直跟着当前栈的。
我们可以回忆一下这个过程。为了及时获得每一对栈的操作的最小值结果，我们需要其实时跟进。
拿空间换时间。
'''


class MinStack:
    def __init__(self):
        self.stack = []
        self.aux_stack = []

    def push(self, val):
        if len(self.stack) == 0:
            self.stack.append(val)
            self.aux_stack.append(val)
        else:
            self.stack.append(val)
            temp = val if val < self.aux_stack[-1] else self.aux_stack[-1]
            self.aux_stack.append(temp)

    def pop(self):
        self.stack.pop(-1)
        self.aux_stack.pop(-1)

    def min(self):
        print(self.aux_stack[-1])


if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(3)
    min_stack.min()
    min_stack.push(4)
    min_stack.min()
    min_stack.push(2)
    min_stack.min()
    min_stack.push(1)
    min_stack.min()
    min_stack.pop()
    min_stack.min()
    min_stack.pop()
    min_stack.min()
    min_stack.push(0)
    min_stack.min()
