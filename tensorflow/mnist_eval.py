#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: mnist_eval.py
@Time: 2017/12/10 21:29
"""

import time
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 再加载自己写的
from Demo_tensorflow.chapter5.section_5 import mnist_inference
from Demo_tensorflow.chapter5.section_5 import mnist_train

"""
加载模型如何操作
导入包的时候，先加载包，在加载自己写的
"""

# 定义加载模型的时间，这里每10秒加载一次
EVAL_INTERVAL_SECS = 10


# evaluate评估的意思
def evaluate(mnist):

    #  1、简介2、不会因为操作逻辑过程，而忘了加入重要的结束语句
    # TODO：最后应该有关闭图或者回话的操作
    with tf.Graph().as_default() as g:
        x = tf.placeholder(tf.float32, shape=[None, mnist_inference.INPUT_NODE], name="x-input")
        y_ = tf.placeholder(tf.float32, shape=[None, mnist_inference.OUTPUT_NODE], name="y-output")

        # 获取验证集
        validate_feed = {x: mnist.validation.images,
                         y_: mnist.validation.labels}

        # 通过模型获得的结果，而且没有正则化了，因为只是调用已经训练好的参数，进行求值
        y = mnist_inference.inference(x, None)

        # 计算准确率等问题。先算分类，再算准确率。 都是个抽像的方法，并没有加入具体的数字去操作
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        # 如何加载模型
        variable_averages = tf.train.ExponentialMovingAverage(mnist_train.MOVING_AVERAGE_DECAY)
        variable_averages_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variable_averages_restore)

        # 每10秒检测加载后的模型，并计算相应的准确率
        while True:
            with tf.Session() as sess:
                ckpt = tf.train.get_checkpoint_state(mnist_train.MODEL_SAVE_PATH)
                if ckpt and ckpt.model_check_path:
                    saver.restore(sess, ckpt.model_check_path)
                    # TODO:gloabl_step是迭代的轮数
                    global_step = ckpt.model_check_path.split("/")[-1].split("-")[-1]
                    # 重新计算得到准确率
                    accuracy_restore = sess.run(accuracy, feed_dict=validate_feed)
                    print("After %d training steps, loss on validation"
                          "batch is %g." % (global_step, accuracy_restore))
                else:
                    print("No checkpoint file found")
                    return
                time.sleep(EVAL_INTERVAL_SECS)


if __name__ == '__main__':
    mnist = input_data.read_data_sets("/tmp/data", one_hot=True)
    eval(mnist)
