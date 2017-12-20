#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: TFLearn_iris.py
@Time: 2017/12/20 13:16
"""

# 导入这么多复杂的
from sklearn import model_selection
from sklearn import datasets
from sklearn import metrics
import tensorflow as tf
import numpy as np
from tensorflow.contrib.learn.python.learn.estimators.estimator import SKCompat

# TODO:fucking world 为什么要这样子导入？？？
import tensorflow.contrib.learn as learn
import tensorflow.contrib.framework as framework
import tensorflow.contrib.layers as layers


def my_model(features, target):
    target = tf.one_hot(target, 3, 1, 0)
    # 预测值
    logits = layers.fully_connected()
    loss = tf.losses.softmax_cross_entropy()

    train_op = layers.optimize_loss(
        loss,
        framework.get_global_step(),
        optimizer="Adam",
        learning_rate=0.01
    )
    return tf.argmax(logits, 1), loss, train_op

iris = datasets.load_iris()
x_train, x_test, y_train, y_test = model_selection.train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=0
)

# 要对原始数据进行类型的转化
x_train, x_test = map(np.float32, [x_train, x_test])

# 封装模型，输出准确率
# classifier = SKCompat(learn.Estimator(model_fn=my_model, model_dir="D:/Python/Demo_tensorflow/chapter8/Models"))
classifier = SKCompat(learn.Estimator(model_fn=my_model, model_dir="D:/Python/Demo_tensorflow/chapter8/Models"))
classifier.fit(x_train, y_train, steps=800)

y_predicted = [i for i in classifier.predict(x_test)]
score = metrics.accuracy_score(y_test, y_predicted)
print('Accuracy: %.2f%%' % (score * 100))
