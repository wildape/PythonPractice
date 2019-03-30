#!/usr/bin/env python3
# encoding: utf-8
import matplotlib.pyplot as plt
import numpy as np
"""
次坐标轴
https://morvanzhou.github.io/tutorials/data-manipulation/plt/4-4-sencondary-axis/
"""
# 第一个y坐标
x = np.arange(0, 10, 0.1)
y1 = 0.05 * x ** 2
y2 = -1 * y1

fig, ax1 = plt.subplots()

# 第二个y坐标
# 对ax1调用twinx()方法，生成如同镜面效果后的ax2:
ax2 = ax1.twinx()

ax1.plot(x, y1, 'g-')  # green, solid line
ax1.set_xlabel('x data')
ax1.set_ylabel('y1 data', color='g')
ax2.plot(x, y2, 'b-')  # blue
ax2.set_ylabel('y2 data', color='b')

plt.show()


