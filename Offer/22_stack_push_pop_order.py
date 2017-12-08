#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 22_stack_push_pop_order.py
@Time: 2017/12/7 16:38
"""
'''
Q:  判断pop_list 是否是 push_list 的一个弹出顺序？
思路：多个辅助栈，很多时候，简单的多个空间的使用，就能解决问题，要有这种意识
对序列的操作，可以用栈来辅助
实现想不到思路的时候，用两个简单的例子去实践下，就有结果了

快做到有思路就写的出来的阶段了:从计算机的角度去处理问题，不能总是想着公式啥的去解决问题

如果这道题判断表面的数字特征就是一件非常复杂的事情，
就脱离了计算机的角度去处理问题，总是同计算机强大计算能力去处理问题
'''


# 今天一定要攻克这个困难！！！
# TODO：类似于指针的思维去处理问题
def is_pop_order(push_list, pop_list):
    # 数组长度
    length = len(push_list)
    aux_stack = []
    # push_list的指针
    p_push = 1
    # pop_list的指针
    p_pop = 0

    # 先把push的第一个给push进去
    aux_stack.append(push_list[0])
    while p_pop < length:
        while p_push < length + 1:
            if pop_list[p_pop] == aux_stack[-1]:
                p_pop += 1
                aux_stack.pop(-1)
                break
            if p_push < length:
                aux_stack.append(push_list[p_push])
                p_push += 1
            if p_push == 5:
                p_push = 5
                if pop_list[p_pop] != aux_stack[-1]:
                    return False

    if p_pop == length:
        return True
    else:
        return False


if __name__ == '__main__':
    push_list = [1, 2, 3, 4, 5]
    pop_list1 = [4, 5, 3, 2, 1]
    pop_list2 = [4, 3, 5, 1, 2]

    print(is_pop_order(push_list, pop_list1))
    print(is_pop_order(push_list, pop_list2))
