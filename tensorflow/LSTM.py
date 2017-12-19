#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com
@File: LSTM.py
@Time: 2017/12/19 9:20
"""
import tensorflow as tf

"""
long short-term memory
"""

# 参数定义
lstm_hidden_size = 3
batch_size = 0
num_steps = 10  # 表示10个以后会被截断
current_input = 0

# 相当于里面的循环体
lstm = tf.nn.rnn_cell.BasicLSTMCell(lstm_hidden_size)
state = lstm.zero_state(batch_size, tf.float32)

# 定义循环函数
loss = 0.0

# 复用前面变量
for i in range(num_steps):
    if i > 0:
        tf.get_variable_scope().reuse_variables()

    lstm_output, state = lstm(current_input, state)

    # TODO:定义的全连接层
    fully_connected = 0

    final_state = fully_connected(lstm_output)

    # 计算损失函数
