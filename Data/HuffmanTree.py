#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: HuffmanTree.py
@Time: 2017/12/15 19:32
"""
"""
    构造哈夫曼树，注意到需要用到最小堆的结论
"""
# 先用排序的方式去做这个问题，再考虑用堆得问题去做


class TreeNode:
    def __init__(self, weight):
        self.weight = weight
        self.left = None
        self.right = None


class HuffmanTree:
    def __init__(self):
        self.huffman_queue = []
        self.size = 0
        self.root = None

    def union(self, vals):
        # 把节点加入列表
        for val in vals:
            self.size += 1
            self.huffman_queue.append(TreeNode(weight=val))
        self.huffman_queue.sort(key=lambda obj:obj.weight)
        while len(self.huffman_queue) > 1:
            node1 = self.huffman_queue.pop(0)
            node2 = self.huffman_queue.pop(0)
            new_node = TreeNode(node1.weight + node2.weight)
            new_node.left = node1
            new_node.right = node2
            self.huffman_queue.append(new_node)
            self.huffman_queue.sort(key=lambda obj:obj.weight)
            self.root = new_node

    def get_root(self):
        print(self.root.weight)

    def in_rec_core(self, root):
        if not root:
            return
        self.in_rec_core(root.left)
        print(root.weight, end=" ")
        self.in_rec_core(root.right)


if __name__ == '__main__':
    hmt = HuffmanTree()
    hmt.union([5,4,3,2,1])
    hmt.get_root()
    hmt.in_rec_core(hmt.root)
