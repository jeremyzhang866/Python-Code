#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com
@File: UnionFindCollection.py
@Time: 2017/12/15 16:54
"""
"""
    实现一个简单的并查集。不考虑重复的元素，毕竟结合就是没有重复的元素
    分析：数组下标表示父亲位置
    链表还是比较容易乱
"""


# 简单的指向双亲的节点
class PaMaNode:
    def __init__(self, val):
        self.val = val
        self.parent = -1
        self.amount = 1


class UnionFindCollection:
    # TODO：链表形式写的，还可以数组形式去写。这样更快
    def __init__(self):
        self.set = []
        self.size = 0

    # 初始化数组
    def init_nums(self, nums):
        for num in nums:
            self.set.append(PaMaNode(num))
            self.size += 1

    # 合并两个元素
    def union(self, val1, val2):
        # 找到根节点对象
        # TODO:注意引用的作用，就是通过引用去解决对象本身的问题
        root1 = self.find(val1)
        root2 = self.find(val2)
        if root1.val == root2.val:
            print("%d 和 %d这两个节点在同一个集合中" %(val1, val2))
        else:
            # 这样比较平衡，总是保证，把总数小的结合
            # TODO:引入了新的节点，是否可以不加入来节省空间
            if root2.amount >= root1.amount:
                root1.parent = root2
                root2.amount += 1
            else:
                root2.parent = root1
                root1.amount += 1

    def find(self, val):
        '''
        查找x坐在集合的父节点
        :param node: 待查找的节点[
        :return: 返回父亲
        '''

        for i in range(self.size):
            if self.set[i].val == val:
                node = self.set[i]
                if node.parent == -1:
                    return node
                else:
                    return self.find_core(node.parent)

    def find_core(self, node):
        if node.parent == -1:
            return node
        else:
            self.find_core(node.parent)

    # 打印
    def show(self):
        for i in range(self.size):
            print(self.set[i].parent, end=" ")


if __name__ == '__main__':
    ufc = UnionFindCollection()
    ufc.init_nums([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # ufc.show()
    ufc.union(5, 6)
    ufc.union(5, 4)
    ufc.union(5, 6)
    root_1 = ufc.find(6)
