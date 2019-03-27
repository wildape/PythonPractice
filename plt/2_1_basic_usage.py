import matplotlib.pyplot as plt
import numpy as np

'''
https://morvanzhou.github.io/tutorials/data-manipulation/plt/2-1-basic-usage/
'''
# 使用np.linspace定义x：范围是(-1,1);个数是50. 仿真一维数据组(x ,y)表示曲线1.
x = np.linspace(-1, 1, 50)
y = 2 * x + 1
# 使用plt.figure定义一个图像窗口
plt.figure()
plt.plot(x, y)
plt.show()


