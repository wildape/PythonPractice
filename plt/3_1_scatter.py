#!/usr/bin/env python3
# encoding: utf-8
import matplotlib.pyplot as plt
import numpy as np

"""
  散点图
  https://morvanzhou.github.io/tutorials/data-manipulation/plt/3-1-scatter/
"""
# 生成数据
'''
生成1024个呈标准正态分布的二维数据组 (平均数是0，方差为1) 作为一个数据集
'''
n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
# color value
T = np.arctan2(Y, X)

plt.scatter(X, Y, s=75, c=T, alpha=.5)
plt.xlim(-1.5, 1.5)
# ignore xticks
plt.xticks(())
plt.ylim(-1.5, 1.5)
# ignore xticks
plt.yticks(())

plt.show()
