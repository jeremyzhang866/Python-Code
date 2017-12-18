#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: Graph_Linked_List.py
@Time: 2017/12/15 19:16
"""


# 邻接链表实现图算法
class Node:
    def __init__(self, val):
        self.val = val
        self.status = "UNDECIDED"
        self.next = None


class Graph:
    # 暂不考虑重复的点
    def __init__(self):
        self.graph = []
        self.status = []
        self.size = 0
        self.VISITED = []
        self.dist = []
        self.path = []

    # 用列表去初始化
    def init_vertex(self, vals):
        for i in range(len(vals)):
            self.status.append("UNDISCOVERED")
        for val in vals:
            node = Node(val)
            node.status = self.status[val - 1]
            self.graph.append(node)
            self.size += 1
            self.VISITED.append(False)
            self.dist.append(-1)
            self.path.append(0)

    # 增加顶点
    def add_vertex(self, val):
        node = Node(val)
        self.graph.append(Node(val))
        self.size += 1

    def init_edges(self, val1, val2s):
        '''
        初始化边
        :param val1:源点
        :param val2s:源点要连的边
        :return:
        '''
        for i in range(self.size):
            if self.graph[i].val == val1:
                p = self.graph[i]
                while p.next:
                    p = p.next
                for val2 in val2s:
                    node = Node(val2)
                    node.status = self.status[val2 - 1]
                    p.next = node
                    # 注意这里的next要继续
                    p = p.next

    # 考虑有向边
    def add_edge(self, val1, val2):
        # 要连接的两个边
        for i in range(self.size):
            if self.graph[i].val == val1:
                # 再对该节点所处的链表进行遍历
                p = self.graph[i]
                while p.next:
                    p = p.next
                p.next = Node(val2)

    def show(self):
        for i in range(self.size):
            p = self.graph[i]
            print(p.val, end=" ")
            while p.next:
                p = p.next
                print("->", p.val, end=" ")
            print()

    def bfs_show(self, source):
        node = self.find(source)
        queue = []
        queue.append(node)
        self.VISITED[source - 1] = True
        while queue:
            # 找到外面的那个对象。注意是外面的那一层东西
            temp_node = queue.pop(0)
            node = self.find(temp_node.val)
            print(node.val, end="  ")
            while node.next:
                if not self.VISITED[node.next.val - 1]:
                    queue.append(node.next)
                    # TODO：注意到这里只是把数组上后面连接的节点的状态变成了"DISCOVERED"
                    self.VISITED[node.next.val - 1] = True
                node = node.next

    def find(self, source):
        # 找到值所对应的节点
        node = Node(-1)
        # 获得源点所对应的节点
        for i in range(self.size):
            if self.graph[i].val == source:
                node = self.graph[i]
                return node
        if node.val == -1:
            print("没有这样的源点")
            return

    def dfs_show(self, source):
        node = self.find(source)
        self.VISITED[source - 1] = True
        print(node.val, end=" ")
        while node.next:
            if not self.VISITED[node.next.val - 1]:
                self.dfs_show(node.next.val)
            node = node.next

    # 无权图单源最短路径
    def unweighted_shortest_graph_sore(self, source):
        node = self.find(source)
        queue = []
        queue.append(node)
        self.dist[source - 1] = 0
        self.path[source - 1] = 0
        while queue:
            # 找到外面的那个对象。注意是外面的那一层东西
            temp_node = queue.pop(0)
            node = self.find(temp_node.val)
            # print(node.val, end="  ")
            while node.next:
                if self.dist[node.next.val - 1] == -1:
                    queue.append(node.next)
                    # TODO：注意到这里只是把数组上后面连接的节点的状态变成了"DISCOVERED"

                    # 上一个节点加一，而且是外面的节点
                    self.dist[node.next.val - 1] = self.dist[temp_node.val - 1] + 1
                    self.path[node.next.val - 1] = temp_node.val
                node = node.next

    # 输出从某一个源头到某一个结尾的路径
    # 当不连通时，输出就挂了
    def unweighted_shortest_graph(self, start, end):
        self.unweighted_shortest_graph_sore(start)
        path = [end]
        while self.path[end - 1] != 0:
            end = self.path[end - 1]
            path.append(end)
        path.reverse()
        print(path)


if __name__ == '__main__':
    graph = Graph()
    vertexs = [1, 2, 3, 4, 5, 6, 7]
    graph.init_vertex(vertexs)
    graph.init_edges(1, [2, 4])
    graph.init_edges(2, [4, 5])
    graph.init_edges(3, [1, 6])
    graph.init_edges(4, [3, 5, 6, 7])
    graph.init_edges(5, [7])
    graph.init_edges(7, [6])
    graph.bfs_show(3)

    # 注意到当bfs操作后，self.visited数组也进行了修正。
    graph.dfs_show(1)


    # 1 -> 2 -> 4
    # 2 -> 4 -> 5
    # 3 -> 1 -> 6
    # 4 -> 3 -> 5 -> 6 -> 7
    # 5 -> 7
    # 6
    # 7 -> 6
