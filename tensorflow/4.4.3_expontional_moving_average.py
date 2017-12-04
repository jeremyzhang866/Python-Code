#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 4.4.3_expontional_moving_average.py
@Time: 2017/12/4 16:27
"""

import tensorflow as tf

# 滑动平均模型
# decay衰减率

# 手动设置类型，并且初始化的时候是0。
v1 = tf.Variable(0, dtype=tf.float32)

# TODO：后面变量什么意思？
step = tf.Variable(0, trainable=False)

ema = tf.train.ExponentialMovingAverage(0.99, step)

# TODO:定义一个操作？？？操作也是可以被定义的？？？而且操作中，带着相应的变量
# 而且下面列表中的变量都会被更新
maintain_averages_op = ema.apply([v1])

with tf.Session() as sess:

    # 初始化所有变量
    init_op = tf.global_variables_initializer()
    # 初始化完了后，要在session中run。
    sess.run(init_op)

    # print(sess.run([v1, ema.average(v1)]))

    # 更新变量v1 到 5，通过assgin的操作
    sess.run(tf.assign(v1, 5))

    sess.run(maintain_averages_op)
    print(sess.run([v1, ema.average(v1)]))
