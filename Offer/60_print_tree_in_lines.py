#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 60_print_tree_in_lines.py
@Time: 2017/11/30 16:01
"""
from Demo_data_algo.Data.Tree.TreeNode import TreeNode


def lever_order(root):
    queue = []
    queue.append(root)
    queue_cache = []
    len_list = [1]
    element_list = []
    while True:

        if (len(queue_cache) == 0) and (len(queue) == 0):
            break

        if queue:
            node = queue.pop(0)
            element_list.append(node.val)
            if node.left: queue_cache.append(node.left)
            if node.right: queue_cache.append(node.right)
        else:
            queue.extend(queue_cache)
            len_list.append(len(queue_cache))
            queue_cache = []
    return element_list, len_list


# 输出每一层元素
# 输出每层的均值
def out_lay_ele(root):
    element_list, len_list = lever_order(root)
    right_index_list = [sum(len_list[:i + 1]) for i in range(len(len_list))]

    left_index_list = [sum(len_list[:i]) for i in range(len(len_list))]
    for i in range(len(len_list)):
        print(element_list[left_index_list[i]:right_index_list[i]])


if __name__ == "__main__":
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(2)
    root.left.left, root.right.right = TreeNode(3), TreeNode(3)
    root.left.right, root.right.left = TreeNode(4), TreeNode(4)
    out_lay_ele(root)
