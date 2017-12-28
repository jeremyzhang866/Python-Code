#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 66_string_path_in_matrix.py
@Time: 2017/12/8 14:06
"""
"""
    矩阵中的路径
    回溯法的经典用法，是后面很多高级方法的一个抽象
    所谓回溯就是，往往跟标志有关，而且基本都是递归
    和图的深度优先遍历区别不大。
"""
import numpy as np


class RecallMatrix:
    def __init__(self, matrix, rows, cols):
        self.matrix = matrix
        self.rows = rows
        self.cols = cols
        self.flag = False

    def has_path(self, path):
        """
        判断是否存在某条路径
        :param path: 带搜索的字符串
        :return: 返回布尔比变量
        """

        # 将字符串转化成了相应row 和 col 的矩阵
        matrix = np.reshape(self.matrix, (self.rows, self.cols))
        for row in range(self.rows):
            for col in range(self.cols):

                # 输入的参数不可以是空的字符串
                # 从矩阵中找到第一个字符
                if matrix[row][col] == path[0]:
                    self.search(matrix, path[1:], [(row, col)], row, col)

                    # 类似于一个全局变量的标志
                    if self.flag:
                        return True
        # 当搜索完矩阵中，path第一个字符所有的路径后，都返回不了true
        # 或者就返回不了true，则直接置为false
        return False

    def search(self, matrix, path, visted, i, j):
        """
        递归核心代码
        :param matrix:待搜索矩阵
        :param path: 目标path
        :param visted:表示已经搜索过的地方
        :param i:当前的出发点的横坐标
        :param j:当前的出发点的纵坐标
        :return:boolean变量
        """
        if path == "":
            self.flag = True
            return

        # 递推关系
        if (j != 0) and ((i, j - 1) not in visted) and (matrix[i][j - 1] == path[0]):
            self.search(matrix, path[1:], [(i, j - 1)] + visted, i, j - 1)

        if (i != 0) and ((i - 1, j) not in visted) and (matrix[i - 1][j] == path[0]):
            self.search(matrix, path[1:], [(i - 1, j)] + visted, i - 1, j)

        if (j != self.cols - 1) and ((i, j + 1) not in visted) and (matrix[i][j + 1] == path[0]):
            self.search(matrix, path[1:], [(i, j + 1)] + visted, i, j + 1)

        if (i != self.rows - 1) and ((i + 1, j) not in visted) and (matrix[i + 1][j] == path[0]):
            self.search(matrix, path[1:], [(i + 1, j)] + visted, i + 1, j)


def main():
    matrix = list("abcesfcfadee")
    rows = 3
    cols = 4
    string = "abcefsgg"
    re_matrix = RecallMatrix(matrix, rows, cols)
    res = re_matrix.has_path(string)
    print(res)


def fake():
    matrix = list("abcesfcfadee")
    matrix = np.reshape(matrix, (3, 4))
    print(matrix)


if __name__ == '__main__':
    main()
