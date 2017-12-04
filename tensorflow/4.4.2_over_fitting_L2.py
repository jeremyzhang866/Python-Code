#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 4.4.2_over_fitting_L2.py
@Time: 2017/12/4 16:20
"""


# 计算一个5层神经网络的L2正则项，损失函数
import tensorflow as tf


# λ alt + 42699
# 正则化化项失效
def get_weight(shape, λ):
    pass


batch_size = 8

x = tf.placeholder(tf.float32, shape=(None, 2))
y_ = tf.placeholder(tf.float32, shape=(None, 1))

# 定下每层的神经元数和层数，注意到输入层是2， 输出层是1
layer_dimension = [2, 10, 10, 10, 1]
n_layers = len(layer_dimension)

# 用来维护前向传播最深入的点，我们初始化输入层
cur_layer = x
# 意为：输入维度
in_dimension = layer_dimension[0]

# 通过循环构建神经网络
# 在构建网络的时候，就已经把参数的正则化项，获得了
# 一次构建，获得更多的信息
for i in range(1, n_layers):
    # 获得输出时的维度
    out_dimension = layer_dimension[i]

    weight = get_weight([in_dimension, out_dimension], 0.001)
    bias = tf.constant(0.1, shape=[out_dimension])

    cur_layer = tf.nn.relu(tf.matmul(cur_layer, weight), bias)
    in_dimension = layer_dimension[i]

# 下面获得损失函数
mse_loss = tf.reduce_mean(tf.square(y_ - cur_layer))

# 将最后一个军方误差加入到losses这个损失函数的集合中去
tf.add_to_collection("losses", mse_loss)
# get_collection() 获得列表
loss = tf.add_n(tf.get_collection("losses"))

tf.contrib.layers.l2_regularizer(alpha)(val)
