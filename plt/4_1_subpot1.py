#!/usr/bin/env python3
# encoding: utf-8
import matplotlib.pyplot as plt
"""
Subplot 多合一显示
https://morvanzhou.github.io/tutorials/data-manipulation/plt/4-1-subpot1/
"""

plt.figure("subplot")
# 使用subplot来创建小图，plt.subplot(2,2,1)表示将整个图像窗口分为2行2列，当前位置为1
# 使用plt.plot([0, 3],[0, 4])在第一个位置创建一个小图
plt.subplot(2, 2, 1)
plt.plot([0, 3], [0, 4])

plt.subplot(2, 2, 2)
plt.plot([0, 1], [0, 2])

plt.subplot(223)
plt.plot([0, 1], [0, 3])

plt.subplot(224)
plt.plot([0, 1], [0, 4])
plt.show()


# 不均匀图中图
# 使用plt.subplot(2,1,1)将整个图像窗口分为2行1列, 当前位置为1. 使用plt.plot([0,1],[0,1])在第1个位置创建一个小图
plt.subplot(211)
plt.plot([0, 1], [0, 1])
'''
上一步中使用plt.subplot(2,1,1)将整个图像窗口分为2行1列, 第1个小图占用了第1个位置, 也就是整个第1行. 
这一步中使用plt.subplot(2,3,4)将整个图像窗口分为2行3列, 于是整个图像窗口的第1行就变成了3列, 
也就是成了3个位置, 于是第2行的第1个位置是整个图像窗口的第4个位置.
'''
plt.subplot(234)
plt.plot([0, 1], [0, 2])

plt.subplot(235)
plt.plot([0, 1], [0, 3])

plt.subplot(236)
plt.plot([0, 1], [0, 4])

plt.show()

