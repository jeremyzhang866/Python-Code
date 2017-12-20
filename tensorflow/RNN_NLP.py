#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: NLP.py
@Time: 2017/12/19 10:00
"""
import numpy as np
import tensorflow as tf
import Demo_tensorflow.chapter8.reader as reader
from tensorflow.contrib.legacy_seq2seq.python.ops.seq2seq import sequence_loss_by_example


# 定义各种参数
DATA_PATH = "D:/Python/Demo_tensorflow/chapter8/data"
HIDDEN_SIZE = 200   # 隐藏层大小
NUM_LAYERS = 2  # LSTM的层数
VOCAB_SIZE = 10000

LEARNING_RATE = 1
TRAIN_BATCH_SIZE = 20
TRAIN_NUM_STEP = 35     # 截断的长度

# 测试集参数设置
EVAL_BATCH_SIZE = 1
EVAL_NUM_STEP = 1
NUM_EPOCH = 2    # 训练数据训练的轮数
KEEP_PRO = 0.5   # 设置drop的参数
MAX_GRAD_NORM = 5   # TODO：控制梯度膨胀的参数


# 描述模型，方便维护
class PTBModel(object):
    def __init__(self, is_training, batch_size, num_steps):
        self.batch_size = batch_size
        self.num_steps = num_steps

        self.input_data = tf.placeholder(tf.int32, [batch_size, num_steps])
        self.targets = tf.placeholder(tf.int32, [batch_size, num_steps])

        # 一行代码实现LSTM模型，并且考虑了dropout和deepRNN以及是否是训练过程
        lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(HIDDEN_SIZE)
        if is_training:
            # TODO：注：这里为什么是output_keep_prob的    概率呢？
            lstm_cell = tf.nn.rnn_cell.DropoutWrapper(lstm_cell, output_keep_prob=KEEP_PRO)
        cell = tf.nn.rnn_cell.MultiRNNCell([lstm_cell] * NUM_LAYERS)

        # TODO：初始状态为什么是batch_size个？
        self.initial_state = cell.zero_state(batch_size, tf.int32)

        # TODO:word2vec技术 为什么维度是这个？
        embedding = tf.get_variable("embedding", [VOCAB_SIZE, HIDDEN_SIZE])
        inputs = tf.nn.embedding_lookup(embedding, self.input_data)
        if is_training:
            inputs = tf.nn.dropout(inputs, KEEP_PRO)

        # 用于存储num_step个值产生的所有的输出，并计算损失函数
        outputs = []
        # 用于记录每个循环体的状态变化，用类自身的进行初始化
        state = self.initial_state
        with tf.variable_scope("RNN"):
            for time_step in range(num_steps):
                if time_step > 0:
                    tf.get_variable_scope().reuse_variables()
                cell_output, state = cell(inputs[:, time_step, :], state)
                outputs.append(cell_output)

        # TODO:将输出reshape为一个这样的形式，从而进行后续操作？为什么要这样的形式
        output = tf.reshape(tf.concat(1, outputs), [-1, HIDDEN_SIZE])

        # 全连接神经网络，而且这没有初始化
        weights = tf.get_variable("weights", [HIDDEN_SIZE, VOCAB_SIZE], tf.float32)
        biases = tf.get_variable("biases", [VOCAB_SIZE])
        logits = tf.matmul(output, weights) + biases

        # 定义交叉熵函数，而且结合了权重
        loss = sequence_loss_by_example(
            [logits],
            [tf.reshape(self.targets, [-1])],
            # 注意权重
            [tf.ones([batch_size * num_steps], dtype=tf.float32)]
        )

        # 计算平均损失
        self.cost = tf.reduce_sum(loss) / batch_size
        self.final_state = state    # 保留最终的更新状态

        # 如果不是考虑在训练集上的数据，直接返回
        if not is_training:
            return

        training_variables = tf.trainable_variables()
        # 注意到这里是全局的clip，
        grads, _ = tf.clip_by_global_norm(
            tf.gradients(self.cost, training_variables),
            MAX_GRAD_NORM
        )

        # 定义优化方法
        optimizer = tf.train.GradientDescentOptimizer(LEARNING_RATE)
        self.train_op = optimizer.apply_gradients(zip(grads, training_variables))


# 运行操作并返回复杂度的值
def run_epoch(session, model, data, train_op, out_log):
    """
    把模型运行这个问题给抽象出来
    返回的是模型在某个数据下求得的复杂度
    :param session: 会话
    :param model: 模型，包括训练模型和验证模型
    :param data: 数据
    :param train_op: 训练具体步骤
    :param out_log: 是否输出日志 boolean
    :return:模型在某个数据下求得的复杂度
    """
    total_costs = 0.0
    iters = 0
    # TODO:注：这里为什么会直接由代码提示多大，model默认为上面的那个类呢？？？
    state = session.run(model.initial_state)
    for step, (x, y) in enumerate(reader.ptb_producer(data, model.batch_size, model.num_steps)):
        cost, state, _ = session.run([model.cost, model.final_state, train_op],
                                     {model.input_data:x, model.targets:y, model.initial_state:state},)
        total_costs += cost
        iters += model.num_steps
        if out_log and step % 100 == 0:
            print("After %d steps, the perplexity is %.3f" %(step, np.exp(total_costs / iters)))

    return np.exp(total_costs / iters)


def main():
    train_data, valid_data, test_data, _ = reader.ptb_raw_data(DATA_PATH)

    # 计算一个epoch需要训练的次数
    train_data_len = len(train_data)
    train_batch_len = train_data_len // TRAIN_BATCH_SIZE
    train_epoch_size = (train_batch_len - 1) // TRAIN_NUM_STEP

    valid_data_len = len(valid_data)
    valid_batch_len = valid_data_len // EVAL_BATCH_SIZE
    valid_epoch_size = (valid_batch_len - 1) // EVAL_NUM_STEP

    test_data_len = len(test_data)
    test_batch_len = test_data_len // EVAL_BATCH_SIZE
    test_epoch_size = (test_batch_len - 1) // EVAL_NUM_STEP

    initializer = tf.random_uniform_initializer(-0.05, 0.05)
    with tf.variable_scope("language_model", reuse=None, initializer=initializer):
        train_model = PTBModel(True, TRAIN_BATCH_SIZE, TRAIN_NUM_STEP)

    with tf.variable_scope("language_model", reuse=True, initializer=initializer):
        eval_model = PTBModel(False, EVAL_BATCH_SIZE, EVAL_NUM_STEP)

    # 训练模型。
    with tf.Session() as session:
        tf.global_variables_initializer().run()

        train_queue = reader.ptb_producer(train_data, train_model.batch_size, train_model.num_steps)
        eval_queue = reader.ptb_producer(valid_data, eval_model.batch_size, eval_model.num_steps)
        test_queue = reader.ptb_producer(test_data, eval_model.batch_size, eval_model.num_steps)

        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=session, coord=coord)

        for i in range(NUM_EPOCH):
            print("In iteration: %d" % (i + 1))
            run_epoch(session, train_model, train_queue, train_model.train_op, True, train_epoch_size)

            valid_perplexity = run_epoch(session, eval_model, eval_queue, tf.no_op(), False, valid_epoch_size)
            print("Epoch: %d Validation Perplexity: %.3f" % (i + 1, valid_perplexity))

        test_perplexity = run_epoch(session, eval_model, test_queue, tf.no_op(), False, test_epoch_size)
        print("Test Perplexity: %.3f" % test_perplexity)

        coord.request_stop()
        coord.join(threads)

# def main():
#     # 从github得到reader函数
#     train_data, valid_data, test_data, _ = reader.ptb_raw_data(DATA_PATH)
#
#     # 定义初始化函数
#     initializer = tf.random_uniform_initializer(-0.05, 0.05)
#
#     with tf.variable_scope("language_model", reuse=None, initializer=initializer):
#         train_model = PTBModel(True, TRAIN_BATCH_SIZE, TRAIN_NUM_STEP)
#
#     with tf.variable_scope("language_model", reuse=True, initializer=initializer):
#         eval_model = PTBModel(False, EVAL_BATCH_SIZE, EVAL_NUM_STEP)
#
#     with tf.Session() as sess:
#         tf.initialize_all_variables().run()
#
#         for i in range(NUM_EPOCH):
#             print("In iteration : %d " % (i + 1))
#
#             # 会输出日志
#             run_epoch(sess, train_model, train_data, train_model.train_op, True)
#
#             valid_perplexity = run_epoch(sess, eval_model, valid_data, tf.no_op(), False)
#             print("Epoch: %d Validation Perplexity: %.3f" %(i + 1, valid_perplexity))
#
#         test_perplexity = run_epoch(sess, eval_model, test_data, tf.no_op(), False)
#         print()
#         print("Test Perplexity: %.3f" % test_perplexity)


def test():
    train_data, valid_data, test_data, _ = reader.ptb_raw_data(DATA_PATH)
    print(len(train_data))
    print(train_data[:100])
    result = reader.ptb_producer(train_data, 4, 5)
    x, y= result
    print(x)
    print(y)
    # print(z)

if __name__ == '__main__':
    main()
