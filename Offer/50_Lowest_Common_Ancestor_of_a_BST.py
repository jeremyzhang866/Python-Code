#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: Lowest_Common_Ancestor_of_a_BST.py
@Time: 2017/11/22 18:37
 Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is
defined between two nodes v and w as the lowest node in T that has both v and w as
descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5

For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of
itself according to the LCA definition.
"""


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 检测node节点是否在二叉树中出现过
# 对其简单的遍历
def has_node(root, val):
    if root.val == val:
        return True

    found = False
    # 注意判断的条件
    if root.left:
        found = has_node(root.left, val)
    if (root.right) and not found:
        found = has_node(root.right, val)

    return found


# 这样相当于对path有了个简单的操作
# 用回溯法,
def get_node_path(root, val, path):
    if root.val == val:
        path.append(root.val)
        return True

    path.append(root.val)

    # 用布尔变量作flag
    found = False
    if root.left:
        found = get_node_path(root.left, val, path)
    # 如果上面已经找到，且右边的不是None，再去考虑这个问题。
    if (not found) and root.right:
        # 简直脑残，在这种低级的问题上出现错误
        found = get_node_path(root.right, val, path)

    if not found:
        path.pop(-1)

    return found


def get_last_commom_node(path1, path2):
    i = -1
    while (i < len(path1)) and (i < len(path2)):
        if path1[i + 1] != path2[i + 1]:
            return path1[i]
        i += 1


def get_lowest_ancestor(root, node1, node2):
    path1, path2 = [], []
    get_node_path(root, node1, path1)
    get_node_path(root, node2, path2)


    print(path1)
    print(path2)

    res = get_last_commom_node(path1, path2)
    return res



if __name__ == '__main__':
    path1 = [1, 3, 5]
    path2 = [1, 3, 6]
    res = get_last_commom_node(path1, path2)
    # print(res)

    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    res = get_lowest_ancestor(root, 3, 4)
    print(res)
