#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: 5.1_mnist_data.py
@Time: 2017/12/4 18:55
"""

from tensorflow.examples.tutorials.mnist import input_data

# 注意到这里我们就是用的是压缩文件的形式，而不用解压缩，计算机对这个十分敏感
# 这搞出来的是一个类的形式
# 要学会看源代码
mnist = input_data.read_data_sets("D:/Python/Demo_tensorflow/chapter5/MNIST_data", one_hot=True)
# print("training data size: ", mnist.train.num_examples)

batch_size = 100

# 注意一下子返回两个参数
xs, ys = mnist.train.next_batch(batch_size)

print("X shape:", xs.shape)
print("Y shape:", ys.shape)

