#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com
@File: 06_construct_binary_tree.py
@Time: 2017/11/30 17:01
"""
"""
Q:
    给你前序，中序，你重建一下树.
    重建二叉树，是一个很困难的问题
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 实在不明白，为何这么短的代码，可以实现这么强功能？
def construct_tree(pre_order, in_order):

    # 递归出口
    if len(pre_order) == 0:
        return None

    root_val = pre_order[0]
    for i in range(len(in_order)):
        if in_order[i] == root_val:
            break

    # 先别去思考内部数字的问题
    left = construct_tree(pre_order[1:1 + i], in_order[:i])
    right = construct_tree(pre_order[1 + i:], in_order[i + 1:])

    return Node(root_val, left, right)


def post_recu(root):
    if root is None:
        return
    post_recu(root.left)
    post_recu(root.right)
    print(root.val, end=" ")


if __name__ == '__main__':
    pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
    in_order = [4, 7, 2, 1, 5, 3, 8, 6]
    root = construct_tree(pre_order, in_order)
    post_recu(root)
