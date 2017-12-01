#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 63_kth_node_in_bst.py
@Time: 2017/11/30 16:38
"""

# 导入BST树
import numpy as np
from Demo_data_algo.Data.Tree.BST import BST


def in_recu_path(root):
    path = []
    in_recu_core(root, path)
    return path


def in_recu_core(root, path):
    if root is None:
        return
    in_recu_core(root.left, path)
    path.append(root.val)
    in_recu_core(root.right, path)


if __name__ == '__main__':
    BSTtree = BST()
    vals = [np.random.randint(1, 100) for _ in range(20)]
    for val in vals:
        BSTtree.insert_ite(val)
    print(in_recu_path(BSTtree.root))

