#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: Max_Heap.py
@Time: 2017/12/7 9:22
"""

# 堆是一个完全二叉树，可以用数组去模拟整个问题
'''
思路：
实现最大堆
1、维护堆，再插入一个数据的时候，始终保证是最大堆（核心）;
    维护用到递归，递归是一种思想，去处理子问题；
2、建立最大堆，插入的时候也要维护；
3、进行堆排。每次取出最上面元素的时候，还要进行维护;
'''

import numpy as np


# heapify是堆化,使动用法
# 且，这里维护的是某一个特定的点，是默认上面都是成立的
def max_heapify(A, length, i):

    # 注意我们获得的都是节点
    # 获得左右节点
    left = i * 2
    right = i * 2 + 1

    # 用一个临时变量存储最大的元素,这里初始化为父节点
    largest = i

    # 获得左节点和父节点中较大的一个

    # TODO：为什么要多加个长度判断？答：当不符合长度判断时，意为着就已经是叶节点了
    # TODO：我们注意到这里是通过节点的判断了解是否是叶节点或者父节点的。
    if left <= length and (A[left] > A[largest]):
        largest = left

    # 获得三个节点中最大的一个
    # TODO：注意到这里的判断，还必须要先判断长度，应为后面的判断是在前面判断的基础上进行的
    if right <= length and A[right] > A[largest]:
        largest = right

    # 意为着最大的节点不是父节点
    if i != largest:
        # 需要进行交换
        A[i], A[largest] = A[largest], A[i]

        # 需要继续堆化下去
        # 不过需要堆化的元素变了
        # 这里的堆化是需要条件的？需要满足条件才会有堆化，因此
        max_heapify(A, length, largest)


# 这里是对某一个元素所有的元素直接对话，自底向上，从最后一个父节点开始的
def build_max_heap(A, length):
    # H获得最后一个父节点
    i = length // 2
    while i >= 1:
        max_heapify(A, length, i)
        i -= 1


# 堆排序
def heap_sort(A, length):
    i = 0

    while i <= length - 1:
        build_max_heap(A, length - i)
        print(A.pop(1), end=" ")
        # print(A)
        i += 1


if __name__ == '__main__':
    # 辅助一个第0个元素为0
    A = [np.random.randint(1, 100) for _ in range(20)]
    B = [0, 3, 5, 7, 2, 1, 4, 8]

    # length的长度应当为数组的真正长度
    length_A = len(A) - 1 # 9
    length_B = len(B) - 1 # 9

    # build_max_heap(A, length_A)
    # print(A[1:])
    #
    # build_max_heap(B, length_B)
    # print(B[1:])

    heap_sort(A, length_A)
    # heap_sort(B, length_B)
