
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 5.2.1_train_mnist.py
@Time: 2017/12/4 20:10
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# 常数都用大写
# 训练集参数
INPUT_NODE = 784    # 28*28
OUTPUT_NODE = 10        # 输出类别


# 配置神经网络参数
LAYER1_NODE = 500   # 一个隐藏层，500个节点
BATCH_SIZE = 100    # 批量数为100

LEARNING_RATE_BASE = 0.8    # 学习速率为0.8
LEARNING_RATE_DECAY = 0.99  # 学习衰减速率为0.8

REGULARIZATION_RATE = 0.0001    # 正则化系数为0.8
TRAINING_STEPS = 30000      # 训练次数为30000
MOVING_AVERAGE_DECAY = 0.99 # 指数移动平均系数为0.99


# 函数的目的是什么啊？
# 便于计算吗？而且还传入一个avg_class的目的又是啥？作用是什么？
def inference(input_tensor, avg_class, weight1, biases1, weight2, biases2):
    if avg_class is None:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weight1) + biases1)
        return tf.matmul(layer1, weight2) + biases2
    else:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, avg_class.average(weight1)) +
                            avg_class.average(biases1))
        return tf.matmul(layer1, avg_class.average(weight2)) + avg_class.average(biases2)


# mnist的类别是啥？
# 注意卸载train函数内部的语句有哪些
# TODO：所有的东西都是类似于符号计算，还并不是数字的形式
def train(mnist):

    # 注意到这里的命名方式有些特殊，第二行的虽然传进去的是OUTPUT_NODE，但是name却是y-input
    x = tf.placeholder(tf.float32, shape=(None, INPUT_NODE), name="x-input")
    y_ = tf.placeholder(tf.float32, shape=(None, OUTPUT_NODE), name="y-input")

    # 生成隐藏层的参数
    # 初始化的方式，注意到他的标准差是0.1，而且都是把tf的整个命名放在 tf.Variable 中
    weight1 = tf.Variable(tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1))
    biases1 = tf.Variable(tf.constant(0.1, shape=[LAYER1_NODE]))

    # 生成隐藏层的参数，而且注意到和隐藏层的参数初始化是一致的
    weight2 = tf.Variable(tf.truncated_normal([LAYER1_NODE, OUTPUT_NODE], stddev=0.1))
    biases2 = tf.Variable(tf.constant(0.1, shape=[OUTPUT_NODE]))

    # 开始计算在当前的参数条件下的前向传播结果
    # 并且注意到这里的AVG_CLASS 记为NONE
    # 直接调用上面定义的结果，
    # 1、可以考虑平滑6的情况；
    # 2、函数，降低耦合性，可以分别调试
    y = inference(x, None, weight1, biases1, weight2, biases2)

    # 注意后面False的使用
    global_step = tf.Variable(0, trainable=False)

    # 平滑问题
    variable_averages = tf.train.ExponentialMovingAverage(
        MOVING_AVERAGE_DECAY, global_step
    )

    # 找所有的训练数据
    variable_averages_op = variable_averages.apply(tf.trainable_variables())

    # 再考虑使用了滑动平均后的前向传播
    average_y = inference(x, variable_averages, weight1, biases1, weight2, biases2)

    # 再考虑损失函数的问题
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
    cross_entropy_mean = tf.reduce_mean(cross_entropy)

    # TODO:这地方的正则化有点问题，找不到相应的函数
    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
    regularization = regularizer(weight1) + regularizer(weight2)
    loss = cross_entropy_mean + regularization

    # 再设置学习速率
    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE,
        global_step,
        # batch方法，过完一遍整个数据集需要的迭代次数，
        mnist.train.num_examples / BATCH_SIZE,
        # 在在外层定义的这个学习衰减速率
        LEARNING_RATE_DECAY
    )

    # 这里的训练次数什么意思？
    # TODO:得到的结果是什么？
    train_step = tf.train.GradientDescentOptimizer(learning_rate).\
        minimize(loss, global_step=global_step)

    # 每过一遍，反向更新参数
    # TODO:这地方代码什么意思？为什么下面代码要搞个精确率呢？不是有了损失函数吗？
    with tf.control_dependencies([train_step, variable_averages_op]):
        train_op = tf.no_op(name="train")

    correct_prediction = tf.equal(tf.argmax(average_y, 1), tf.argmax(y_, 1))
    accuracy =tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # with在这个函数训练的里面
    with tf.Session() as sess:
        tf.global_variables_initializer().run()

        # feed是供给的意思
        validate_feed = {x: mnist.validation.images,
                         y_:mnist.validation.labels}

        test_feed = {x:mnist.test.images,
                     y_:mnist.test.labels}

        for i in range(TRAINING_STEPS):
            if i % 1000 == 0:
                validate_acc = sess.run(accuracy, validate_feed)
                print("%d training step(s), validation accuracy"
                      "using average model is %g" %(i, validate_acc))

            # 每一轮都会有个新的batch数据
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            sess.run(train_op, feed_dict={x:xs, y_:ys})

        test_acc = sess.run(accuracy, test_feed)
        print("%d training step(s), test accuracy"
              "using average model is %g" % (i, test_acc))


def main(argv = None):
    mnist = input_data.read_data_sets("D:/Python/Demo_tensorflow/chapter5/MNIST_data", one_hot=True)
    train(mnist)


if __name__ == '__main__':
    tf.app.run()
