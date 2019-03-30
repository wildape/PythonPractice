#!/usr/bin/env python3
# encoding: utf-8
import matplotlib.pyplot as plt

"""
Subplot 分格显示
https://morvanzhou.github.io/tutorials/data-manipulation/plt/4-2-subplot2/
"""

plt.figure()
# subplot2grid
'''
 (3,3)表示将整个图像窗口分成3行3列, 
 (0,0)表示从第0行第0列开始作图，colspan=3表示列的跨度为3, 
 rowspan=1表示行的跨度为1. colspan和rowspan缺省, 默认跨度为1.
'''
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax1.plot([1, 2], [1, 2])
ax1.set_title('ax1_title')

'''
使用plt.subplot2grid来创建第2个小图, (3,3)表示将整个图像窗口分成3行3列, (1,0)表示从第1行第0列开始作图，colspan=2表示列的跨度为2. 同上画出 ax3, (1,2)表示从第1行第2列开始作图，rowspan=2表示行的跨度为2. 
再画一个 ax4 和 ax5, 使用默认 colspan, rowspan.
'''
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))

# 使用ax4.scatter创建一个散点图, 使用ax4.set_xlabel和ax4.set_ylabel来对x轴和y轴命名.
ax4.scatter([1, 2], [2, 2])

plt.show()

# gridspec
