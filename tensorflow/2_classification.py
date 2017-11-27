#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 2_classification.py
@Time: 2017/11/27 16:12
"""


import tensorflow as tf
from numpy.random import RandomState

batch_size = 8

w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

# 定义占位符
x = tf.placeholder(tf.float32, shape=(None, 2), name="x-input")
y_ = tf.placeholder(tf.float32, shape=(None, 1), name="y-input")


# 定义前向传播
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)


# 定义损失函数和反向传播的算法
cross_entropy = -tf.reduce_mean(
    y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0))
)
train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)


# 通过随机树生成一个模拟的训练集
# Random保证随机产生的开始是一样的，类似于随机种子的使用，seed = 1 的用法
# 人为随机生成的两个样本
rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)
Y = [[int(x1 + x2 < 1) for (x1, x2) in X]]

with tf.Session() as sess:

    # 真正初始化变量
    init_op = tf.initialize_all_variables()
    sess.run(init_op)

    # 训练之前参数的值
    print(sess.run(w1))
    print(sess.run(w2))

    STEPS = 5000
    for i in range(STEPS):

        # 每次可以选择batch_size个数据进行训练
        start = (i * batch_size) % dataset_size
        end = min(start + batch_size, dataset_size)

        sess.run(
            train_step, feed_dict={x:X[start:end], y_:Y[start:end]}
        )

        # 每个一段时间计算在所有数据上的交叉熵并输出
        if i % 1000:
            total_cross_entropy = sess.run(
                cross_entropy, feed_dict={x:X, y_:Y}
            )
            print("After %d traing steps, cross entropy on all data is %g" %(i, total_cross_entropy))

        print(sess.run(w1))
        print(sess.run(w2))

