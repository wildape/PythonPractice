#!/usr/bin/env python3
# encoding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

"""
Animation 动画
https://morvanzhou.github.io/tutorials/data-manipulation/plt/5-1-animation/
"""

# 定义方程
fig, ax = plt.subplots()
x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


# 构造自定义动画函数animate，用来更新每一帧上各个x对应的y坐标值，参数表示第i帧
def animate(i):
    line.set_ydata(np.sin(x + i / 10.0))
    return line


def init():
    line.set_ydata(np.sin(x))
    return line


# 参数设置
ani = animation.FuncAnimation(fig=fig,
                              func=animate,
                              frames=100,
                              init_func=init,
                              interval=20,
                              blit=False)
plt.show()
