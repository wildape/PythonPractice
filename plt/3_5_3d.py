#!/usr/bin/env python3
# encoding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

"""
3D图
https://morvanzhou.github.io/tutorials/data-manipulation/plt/3-5-3d/
"""

fig = plt.figure()
ax = Axes3D(fig)
# plt.show()
# 接下来给进 X 和 Y 值，并将 X 和 Y 编织成栅格。每一个（X, Y）点对应的高度值我们用下面这个函数来计算。

# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
# x-y平面的网络
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
# height value
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
plt.show()
