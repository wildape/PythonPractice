#!/usr/bin/env python3
# encoding: utf-8
import matplotlib.pyplot as plt
import numpy as np

"""
Bar 柱状图
https://morvanzhou.github.io/tutorials/data-manipulation/plt/3-2-Bar/
"""
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
# plt.bar(X, +Y1)
# plt.bar(X, -Y2)

plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

# plt.show()

# 加颜色和数据
# 用facecolor设置主体颜色，edgecolor设置边框颜色
plt.bar(X, +Y1, facecolor='#00EFFF', edgecolor='white')
plt.bar(X, -Y1, facecolor='#00FF00', edgecolor='white')

# plt.show()
'''
接下来我们用函数plt.text分别在柱体上方（下方）加上数值，
用%.2f保留两位小数，横向居中对齐ha='center'，
纵向底部（顶部）对齐va='bottom'
'''
for x, y in zip(X, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')
plt.show()
