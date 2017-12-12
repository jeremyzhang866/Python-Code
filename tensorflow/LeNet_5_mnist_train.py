#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
    @File: LeNet_5_mnist_train.py
@Time: 2017/12/10 21:29
"""

import os
import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# TODO：文件名导入的时候，很有规律
import Demo_tensorflow.chapter6.LeNet_5_mnist_inference as mnist_inference

# 配置一大堆参数变量，在训练的过程中
BATCH_SIZE = 100

LEARNING_RATE_BASE = 0.8
LEARNING_RATE_DECAY = 0.99

REGULARAZTION = 0.0001

TRAINING_STEPS = 6000
MOVING_AVERAGE_DECAY = 0.99

# TODO：配置模型保存的路径和文件名
MODEL_SAVE_PATH = "D:/Python/Demo_tensorflow/chapter6/model"
MODEL_NAME = "mode.ckpt"


def train(mnist):
    x = tf.placeholder(tf.float32, shape=[
        BATCH_SIZE,
        mnist_inference.IMAGE_SIZE,
        mnist_inference.IMAGE_SIZE,
        mnist_inference.NUM_CHANNELS],
                       name="x-input")

    y_ = tf.placeholder(tf.float32, shape=[
        None,
        mnist_inference.NUM_LABELS], name="y-input")

    regularizer = tf.contrib.layers.l2_regularizer(REGULARAZTION)

    # 获得前向传播的结果
    y = mnist_inference.inference(x, False, regularizer)

    # TODO:global_step。明确指出不需要训练
    global_step = tf.Variable(0, trainable=False)

    # 再配置一堆参数，比如说损失函数，指数衰减式学习率，滑动平均，和训练过程
    variable_averages = tf.train.ExponentialMovingAverage(
        MOVING_AVERAGE_DECAY, num_updates = global_step
    )

    # 应用到需要训练的所有参数
    variable_averages_op = variable_averages.apply(tf.trainable_variables())

    # TODO:损失函数，交叉熵.注：这里的写法和书上不一样，见源码
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
    cross_entropy_mean = tf.reduce_mean(cross_entropy)
    loss = cross_entropy_mean + tf.add_n(tf.get_collection("losses"))

    # 记得要调学习率
    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE,
        global_step,
        mnist.train.num_examples / BATCH_SIZE,
        LEARNING_RATE_DECAY
    )

    train_step = tf.train.GradientDescentOptimizer(learning_rate)\
    .minimize(loss, global_step = global_step)
    train
    # TODO:干啥用的？
    with tf.control_dependencies([train_step, variable_averages_op]):
        train_op = tf.no_op(name="train")

    # 初始化持久类，用于保存模型
    # saver = tf.train.Saver()
    with tf.Session() as sess:
        tf.initialize_all_variables().run()

        # 训练的真正过程
        for i in range(TRAINING_STEPS):
            xs, ys = mnist.train.next_batch(BATCH_SIZE)

            reshaped_xs = np.reshape(xs, (
                BATCH_SIZE,
                mnist_inference.IMAGE_SIZE,
                mnist_inference.IMAGE_SIZE,
                mnist_inference.NUM_CHANNELS))
            # TODO:这里传入的第一个参数是很复杂的情况
            # 而且获得的数字进行了元组拆包
            _, loss_value, step = sess.run([train_op, loss, global_step], feed_dict={x: reshaped_xs, y_: ys})

            # 每1000次，保存一次模型
            # %g的意思是自动选择e or f
            if i % 50 == 0:
                print("After %d training steps, loss on training"
                      " batch is %g." %(step, loss_value))
                # TODO: 这里如何加入系统路径
                # saver.save(sess, os.path.join(""), global_step = global_step)


if __name__ == '__main__':
    mnist = input_data.read_data_sets("/tmp/data", one_hot=True)
    train(mnist)
