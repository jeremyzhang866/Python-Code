 #!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 4.2.2_different_loss_function.py
@Time: 2017/12/4 14:42
"""


import tensorflow as tf
from numpy.random import RandomState

# 确定批量的个数
batch_size = 8


# 考虑输入节点和输出节点
x = tf.placeholder(tf.float32, shape=(None, 2), name="X_input")
# 输出节点为真值
y_ = tf.placeholder(tf.float32, shape=(None, 1), name="y_ouput")

# 定义隐藏层，就一层
w1 = tf.Variable(tf.random_normal([2, 1], stddev=1, seed=1))
# 矩阵乘法顺序有要求吗?
y = tf.matmul(x, w1)

# 自定义损失函数
loss_less = 1
loss_more = 10
loss = tf.reduce_mean(tf.where(tf.greater(y, y_),
                               (y - y_) * loss_more,
                               (y_ - y) * loss_less))
# 优化方法
train_step = tf.train.AdamOptimizer(0.001).minimize(loss)

# 模拟数据
rdm = RandomState(1)
data_size = 128
# 表示2个一组，维度应当与输入的维度是一致的
X = rdm.rand(data_size, 2)
# 为什么要给输出的值加一个随即项
Y = [[x1 + x2 + rdm.rand()/10 - 0.05] for x1, x2 in X]


with tf.Session() as sess:
    # 真正初始化变量
    init_op = tf.initialize_all_variables()
    # 运行代码
    sess.run(init_op)
    STEPS = 5000

    # 批量运行
    for i in range(STEPS):
        start = (i + batch_size) % data_size
        end = min(start + batch_size, data_size)
        sess.run(train_step,
                 feed_dict={x:X[start:end], y_:Y[start:end]})

        # 为什么要最后打印w1?
        print(sess.run(w1))
