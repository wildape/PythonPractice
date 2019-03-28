#!/usr/bin/env python3
# encoding: utf-8

import matplotlib.pyplot as plt
import numpy as np

"""
  tick 能见度
  https://morvanzhou.github.io/tutorials/data-manipulation/plt/2-7-tick-visibility/
"""

x = np.linspace(-3, 5, 50)
y = 0.1 * x

plt.figure()
# zorder z轴排序？
plt.plot(x, y, linewidth=10, zorder=1)
plt.ylim(-2, 2)
ax = plt.gca()
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# 调整坐标
'''
然后对被遮挡的图像调节相关透明度，本例中设置 x轴 和 y轴 的刻度数字进行透明度设置
其中label.set_fontsize(12)重新调节字体大小，bbox设置目的内容的透明度相关参，
facecolor调节 box 前景色，edgecolor 设置边框， 本处设置边框为无，alpha设置透明度.
'''
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    # 在 plt 2.0.2 或更高的版本中, 设置 zorder 给 plot 在 z 轴方向排序
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7, zorder=2))
plt.show()
