#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: BST.py
@Time: 2017/11/30 16:50
搜索树
"""


class TreeNode:
    # 这里的-1是默认值
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 类似于重建一棵树的方式，也是不断的加入一个节点
# 也是递归的加入节点，插入一个节点后，返回新的根节点
def insert(root, val):
    if root is None:
        root = TreeNode(val)
        return root

    if val <= root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)


class BST:
    def __init__(self):
        self.root = None

    # 判断是否为空
    def empty(self):
        if self.root is None:
            return True
        return False

    # 返回根节点
    def get_root(self):
        return self.root

    # 中序遍历的递归形式
    # 注意树里面的对公写法
    def preShow(self, curr_node):
        if curr_node is None:
            return
        self.preShow(curr_node.left)
        print(curr_node.val, end=" ")
        self.preShow(curr_node.right)

    # 插入节点循环形式
    # 循环和递归形式都可以插入节点
    # self加的地方也不是特别多
    def insert_ite(self, val):
        node = TreeNode(val)

        if self.empty():
            self.root = node
        else:

            # 记录用于寻找节点之前的父节点
            # 这种手法有点意思
            curr_dad_node = None
            curr_node = self.root

            while True:
                if curr_node:
                    curr_dad_node = curr_node
                    if node.val <= curr_node.val:
                        curr_node = curr_node.left
                    else:
                        curr_node = curr_node.right

                else:
                    if node.val <= curr_dad_node.val:
                        curr_dad_node.left = node
                    else:
                        curr_dad_node.right = node
                    break


if __name__ == '__main__':
    t = BST()
    vals = [8, 3, 1, 6, 4, 7, 10, 14, 13]
    for val in vals:
        print(val, end=" ")
        t.insert_ite(val)
    print()
    t.preShow(t.root)
