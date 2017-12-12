#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: LeNet_5_mnist_inference.py
@Time: 2017/12/10 21:10
"""
"""
    总结CNN经典网络架构设计模式
"""

import tensorflow as tf

# 配置CNN参数，去解决mnist问题
INPUT_NODE = 784
OUT_PUT = 10

# 图片信息
IMAGE_SIZE = 28
NUM_CHANNELS = 1
NUM_LABELS = 10

# CONV Layer filter
CONV1_DEEP = 32
CONV1_SIZE = 5

CONV2_DEEP = 64
CONV2_SIZE = 5

# TODO：FC 全连接层，结点个数？？？为啥呢？
FC_SIZE = 512


def inference(input_tensor, train, regularizer):
    with tf.variable_scope("layer1-conv1"):
        # 就是那个filter
        conv1_weight = tf.get_variable(
            "weight",
            shape=[CONV1_SIZE, CONV1_SIZE, NUM_CHANNELS, CONV1_DEEP],
            initializer=tf.truncated_normal_initializer(stddev=0.1)
        )
        conv1_biases = tf.get_variable(
            "bias",
            shape=[CONV1_DEEP],
            initializer=tf.constant_initializer(0.0)
        )
        conv1 = tf.nn.conv2d(input_tensor, conv1_weight, strides=[1, 1, 1, 1], padding="SAME")
        relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_biases))

    with tf.variable_scope("layer2-pool1"):
        pool1 = tf.nn.max_pool(relu1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")

    with tf.variable_scope("layer3-conv2"):
        # 就是那个filter
        conv2_weight = tf.get_variable(
            "weight",
            # 注意到节点的高变了，变成CONV1_DEEP，也就是上一个卷积层的过滤器的深度
            shape=[CONV2_SIZE, CONV2_SIZE, CONV1_DEEP, CONV2_DEEP],
            initializer=tf.truncated_normal_initializer(stddev=0.1)
        )
        conv2_biases = tf.get_variable(
            "bias",
            shape=[CONV2_DEEP],
            initializer=tf.constant_initializer(0.0)
        )
        conv2 = tf.nn.conv2d(pool1, conv2_weight, strides=[1, 1, 1, 1], padding="SAME")
        relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_biases))

    with tf.variable_scope("layer4-pool2"):
        pool2 = tf.nn.max_pool(relu2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")

    # 两次卷积和池化层后就是全连接层。承上启下的作用
    pool_shape = pool2.get_shape().as_list()
    nodes = pool_shape[1] * pool_shape[2] * pool_shape[3]
    # 拉直后的向量
    reshaped = tf.reshape(pool2, [pool_shape[0], nodes])

    # 构建全连接层
    with tf.variable_scope("layer5-fc1"):
        fc1_weight = tf.get_variable(
            "weight",
            shape=[nodes, FC_SIZE],
            initializer=tf.truncated_normal_initializer(stddev=0.1)
        )
        fc1_biases = tf.get_variable(
            "bias",
            shape=[FC_SIZE],
            initializer=tf.constant_initializer(0.1)
        )

        if regularizer:
            # 只针对权重参数
            tf.add_to_collection("losses", regularizer(fc1_weight))

        fc1 = tf.matmul(reshaped, fc1_weight + fc1_biases)
        if train:
            # 后面参数是概率问题
            fc1 = tf.nn.dropout(fc1, 0.5)

    with tf.variable_scope("layer6-fc2"):
        fc2_weight = tf.get_variable(
            "weight",
            shape=[FC_SIZE, NUM_LABELS],
            initializer=tf.truncated_normal_initializer(stddev=0.1)
        )
        fc2_biases = tf.get_variable(
            "bias",
            shape=[NUM_LABELS],
            initializer=tf.constant_initializer(0.1)
        )
        if regularizer:
            # 只针对权重参数
            tf.add_to_collection("losses", regularizer(fc2_weight))

        logit = tf.matmul(fc1, fc2_weight) + fc2_biases

    return logit
