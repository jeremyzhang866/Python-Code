#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: DoubleCycleLinkedList.py
@Time: 2017/12/9 19:30
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None


class DoubleCycleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # add到末尾
    def add(self, val):
        node = Node(val)
        self.size += 1
        if self.head is None:
            self.head = node
        else:
            p = self.head

            # TODO:找到尾节点，要结合长度，要不就挂了!! 也可以用长度找到尾节点
            count = 1
            while count < self.size - 1:
                p = p.next
                count += 1
            # 后面两个节点连接
            p.next = node
            node.pre = p

            # 将尾节点和头结点连接
            node.next = self.head
            self.head.pre = node

    # 删除某个指标的元素
    def delete_index(self, index):
        if index < 0 or self.size == 0 or index > self.size -1:
            print("delete is failure")
            return

        self.size -= 1
        if index == 0:
            # 要注意有删除pre和next
            self.head.next.pre = None
            self.head = self.head.next
        else:
            p = self.head
            count = 0

            # 找到待删除节点的前一个
            while count < index- 1:
                p = p.next
                count += 1

            # 如果删除的是尾节点
            if p.next.next is None:
                p.next = self.head
                self.head.pre = p
            else:
                # 删除的除了尾节点和节点的数据
                p.next.next.pre = p
                p.next = p.next.next

    def show(self):
        p = self.head
        count = 0
        while count < 3 * self.size:
            print(p.val, end=" ")
            p = p.next
            count += 1

    def show_reverse(self):
        p = self.head

        # 找到了尾节点
        count = 1
        while count < self.size:
            p = p.next
            count += 1

        # 从尾节点到这输出
        count = 0
        while count < 3 * self.size:
            print(p.val, end=" ")
            p = p.pre
            count += 1


if __name__ == '__main__':
    double_ = DoubleLinkedList()
    nums = [1, 2, 3, 4, 5]
    for num in nums:
        double_.add(num)

    double_.delete_index(3)
    double_.show()
    print()
    double_.show_reverse()

    print()
    print("链表长度为： %d" %double_.size)
