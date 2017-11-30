#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 59_symmetrical_tree.py
@Time: 2017/11/30 14:51
Q:
判断是不是对称的二叉树
"""

from Demo_data_algo.Data.Tree.TreeNode import TreeNode

# 这个整体和局部的关系不大

# 利用层次遍历的迭代方法
def is_symmetrical_tree_lever_ite(root):
    if root is None:
        return True

    stack = []
    stack.append(root.left)
    stack.append(root.right)

    # 为了统一，加入这两个元素
    while stack:
        p, q = stack.pop(), stack.pop()

        # 主要是他在前面判断了，所以下面的if -else肯定是不会有两个都是None的情形
        if p is q is None:
            # 当p, q都是None的时候，就continue，不去考虑这个问题
            continue

        if p is None or q is None or p.val != q.val:
            return False

        stack.append(p.left)
        stack.append(q.right)

        stack.append(p.right)
        stack.append(q.left)
    return True

# 利用层次遍历的递归方法
def is_symmetrical_tree_lever_recu(root):
    if root is None:
        return True
    return is_symmetrical_tree_recu_core(root.left, root.right)

# 上述方法的核心方法
def is_symmetrical_tree_recu_core(left, right):
    if left is right is None:
        return True

    if left is None or right is None or left.val != right.val:
        return False

    return is_symmetrical_tree_recu_core(left.left, right.right) and \
           is_symmetrical_tree_recu_core(left.right, right.left)



if __name__ == "__main__":
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(2)
    root.left.left, root.right.right = TreeNode(3), TreeNode(3)
    root.left.right, root.right.left = TreeNode(4), TreeNode(4)
    res1 = is_symmetrical_tree_lever_ite(root)
    res2 = is_symmetrical_tree_lever_recu(root)
    print(res1)
    print(res2)

