#!/usr/bin/env python3
# encoding: utf-8
import numpy as np

'''
sum(), min(), max()
'''
# 产生2行，4列的矩阵，每一个元素来自于(0,1)
a = np.random.rand(2, 4)
print(a)
print(np.sum(a))
print(np.min(a))
print(np.max(a))

# 可以对axis赋值以选择轴进行计算，axis = 1，以行分组计算，axis = 0以列分组计算

# 计算每行的和
print("sum= ", np.sum(a, axis=1))
# 计算每列的和
print("sum= ", np.sum(a, axis=0))

# 计算每列的最小值
print("min= ", np.min(a, axis=0))

'''
基础运算2
ref: https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/2-4-np-math2/
'''

# 索引
a = np.arange(2, 14).reshape(3, 4)
# argmin() 求矩阵中最小元素对于的索引
print(np.argmin(a))  # 0
# argmax() 求矩阵中最大元素对于的索引
print(np.argmax(a))  # 11

# mean()/average()计算均值
print(np.mean(a))  # or a.mean()
print(np.average(a))

# median()中位数
print(np.median(a))

# cumsum()累加函数
print(np.cumsum(a))  # [ 2  5  9 14 20 27 35 44 54 65 77 90]

# diff() 累差函数 该函数计算的便是每一行中后一项与前一项之差。
# 故一个3行4列矩阵通过函数计算得到的矩阵便是3行3列的矩阵。
print(np.diff(a))
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]


