#!/usr/bin/env python3
# encoding: utf-8
import matplotlib.pyplot as plt
import numpy as np

"""
  标注
  https://morvanzhou.github.io/tutorials/data-manipulation/plt/2-6-annotation/
"""

# 当图线中某些特殊地方需要标注时，我们可以使用 annotation. matplotlib 中的 annotation 有两种方法， 一种是用 plt 里面的 annotate，一种是直接用 plt 里面的 text 来写标注.

x = np.linspace(-3, 3, 50)
y = 2 * x + 1

# 画出基本图
plt.figure(num=2, figsize=(8, 5))
plt.plot(x, y)
# plt.show()

# 移动坐标
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

x1 = 1
y1 = 2 * x1 + 1
plt.plot([x1, x1], [0, y1], 'k--', linewidth=2)
# set dot styles
plt.scatter([x1], [y1], s=50, color='blue')
# plt.show()


# 添加注解annotate
'''
对(x1, y1)这个点进行标注
其中参数xycoords='data' 是说基于数据的值来选位置, 
xytext=(+30, -30) 和 textcoords='offset points' 对于标注位置的描述 和 xy 偏差值, 
arrowprops是对图中箭头类型的一些设置.
'''
plt.annotate(r'$2x+1=%s$' % y1, xy=(x1, y1), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
# plt.show()

# 添加注释text
# 其中-3.7, 3,是选取text的位置, 空格需要用到转字符\ ,fontdict设置文本字体.
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})

plt.show()
