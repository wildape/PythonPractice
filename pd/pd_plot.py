import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
Pandas plot 出图
ref: https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/3-8-pd-plot/
'''

'''
创建一个Series
这是一个线性的数据，我们随机生成1000个数据，Series 默认的 index 就是从0开始的整数，
但是这里我显式赋值以便让大家看的更清楚
'''
# 随机生成1000个数据
data = pd.Series(np.random.randn(10000), index=np.arange(10000))

# 为了方便观看效果，累加这个数据
data = data.cumsum()

# pandas 数据可以直接观看其可视化形式
data.plot()
plt.show()

# Dataframe可视化
# 生成1000 * 4的DataFrame，并对它们累加
data = pd.DataFrame(
    np.random.randn(1000, 4),
    index=np.arange(1000),
    columns=list("ABCD")
)
data = data.cumsum()
data.plot()
plt.show()

# 散点图 scatter

ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class1')
data.plot.scatter(x='A', y='C', color='LightGreen', label='Class2', ax=ax)
plt.show()
