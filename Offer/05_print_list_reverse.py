#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 05_print_list_reverse.py
@Time: 2017/12/8 15:48
"""

"""

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list_reverse_ite(node):
    stack = []
    p = node
    stack.append(p.val)
    while p.next:
        stack.append(p.next.val)
        p = p.next
    for i in range(len(stack)):
        print(stack.pop(), end=" ")


def print_list_reverse_rec(node):
    if not node.next:
        print(node.val, end=" ")
        return
    print_list_reverse_ite(node.next)
    print(node.val)


if __name__ == '__main__':
    node = Node(1)
    node.next = Node(2)
    node.next.next = Node(3)
    node.next.next.next = Node(4)
    print_list_reverse_ite(node)
    print()
    print_list_reverse_rec(node)
