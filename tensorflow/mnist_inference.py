#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: mnist_inference.py
@Time: 2017/12/10 21:28
"""


"""
神经网络的前向传播过程，以及参数的定义过程
"""
import tensorflow as tf

# 配置各个神经层的参数
INPUT_NODE = 784
OUTPUT_NODE = 10
LAYER1_NODE = 500


def get_weight_variable(shape, regularizer):
    weight = tf.get_variable(
        "weights",
        shape=shape,
        initializer=tf.truncated_normal_initializer(stddev=0.1)
    )

    if regularizer:
        tf.add_to_collection("losses", regularizer(weight))

    return weight


def inference(input_tensor, regularizer):
    with tf.variable_scope("layer1"):
        weights = get_weight_variable([INPUT_NODE, LAYER1_NODE], regularizer)
        biases = tf.get_variable("biases", shape=[LAYER1_NODE],
                                 initializer=tf.constant_initializer(0.0))
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weights) + biases)

    with tf.variable_scope("layer2"):
        weights = get_weight_variable([LAYER1_NODE, OUTPUT_NODE], regularizer)
        biases = tf.get_variable("biases", shape=[OUTPUT_NODE],
                                 initializer=tf.constant_initializer(0.0))
        layer2 = tf.nn.relu(tf.matmul(input_tensor, weights) + biases)

    return layer2
