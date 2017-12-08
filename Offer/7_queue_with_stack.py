#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 7_queue_with_stack.py
@Time: 2017/12/7 17:14
"""
'''
Q:用两个栈，实现优先队列。实现在头部加入删除节点，尾部加入节点
思路：比较简单，先把核心思想写出来。
'''


class pQueue:
    def __init__(self, A):
        self.stack1 = A
        self.stack2 = []

    def append_tail(self, val):
        self.stack1.append(val)

    def pop_head(self):
        if len(self.stack2) == 0:
            self.stack1.reverse()
            self.stack2 =self.stack1[:]
            self.stack1 = []
            print(self.stack2.pop())
        else:
            print(self.stack2.pop())

if __name__ == '__main__':
    q = pQueue([7, 1,2,3])

    q.pop_head()
    q.append_tail(8)
    q.pop_head()

    q.pop_head()
    q.pop_head()
    q.pop_head()
    q.pop_head()
