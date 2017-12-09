#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 45_last_num_in_circle.py
@Time: 2017/12/9 13:32
"""
"""
Q：
    约瑟夫环问题
"""
# TODO：法一：构造一个环形链表


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class CircleLinkedList:
    def __init__(self):
        self.head = None
        # 这个是它的成员，可以直接获取
        self.size = 0

    # 用一个列表去初始化
    def init_list(self, nums):
        self.head = Node(nums[0])
        self.size = 1

        # 获得一个可以变动的值，是self.head的一个引用
        p = self.head
        for num in nums[1:]:
            p.next = Node(num)
            p = p.next
            self.size += 1
        p.next = self.head

    # 末尾添加一个元素
    def add_ele(self, val):
        self.size += 1
        if self.head is None:
            self.head = Node(val)
        else:
            # 获得头结点的指针
            p = self.head
            count = 0
            # 当是循环的链表的时候，这里的p是一直next的话，就爆炸了
            while p.next and count < self.size - 2:
                p = p.next
                count += 1
            p.next = Node(val)
            p.next.next = self.head

            # p = p.next
            # p.next = self.head

    # 删除某一个元素
    # 注：index可以从0开始，范围到size - 1
    def delete_ele(self, index):
        if self.size == 0 or index < 0 or index >= self.size:
            print("delete is failure")
            return

        # 删除头结点
        if index == 0:
            self.head = self.head.next
            p = self.head
            count = 1
            while p.next and count < self.size - 1:
                p = p.next
                count += 1
            p.next = self.head
        else:
            count = 1
            p = self.head
            while count < index:
                count += 1
                p = p.next
            if p.next.next is None:
                p.next = None
            else:
                p.next = p.next.next
        self.size -= 1

    def show(self):
        p = self.head
        count = 0
        while p and count < 2 * self.size:
            print(p.val, end=" ")
            p = p.next
            count += 1


if __name__ == '__main__':
    nums = range(5)
    cir_linked_list = CircleLinkedList()
    cir_linked_list.init_list(nums)
    cir_linked_list.add_ele(5)
    cir_linked_list.delete_ele(0)
    cir_linked_list.show()
    print()
    print("circle_list length is %d " %cir_linked_list.size)
