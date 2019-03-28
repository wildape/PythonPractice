#!/usr/bin/env python3
# encoding: utf-8
import numpy as np
import pandas as pd

'''
Pandas 合并concat
Ref: https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/3-6-pd-concat/
'''

# axis(合并方向)
'''
axis = 0是默认值， 1 是行，0表示列
'''
# 定义资料集
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])

# concat纵向合并
res = pd.concat([df1, df2, df3], axis=0)
print(res)
#      a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 0  1.0  1.0  1.0  1.0
# 1  1.0  1.0  1.0  1.0
# 2  1.0  1.0  1.0  1.0
# 0  2.0  2.0  2.0  2.0
# 1  2.0  2.0  2.0  2.0
# 2  2.0  2.0  2.0  2.0

# ignore_index(重置index)
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res)
#      a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  1.0  1.0  1.0
# 4  1.0  1.0  1.0  1.0
# 5  1.0  1.0  1.0  1.0
# 6  2.0  2.0  2.0  2.0
# 7  2.0  2.0  2.0  2.0
# 8  2.0  2.0  2.0  2.0


# join 合并方式
'''
join='outer'为预设值，因此未设定任何参数时，函数默认join='outer'。
此方式是依照column来做纵向合并，有相同的column上下合并在一起，
其他独自的column个自成列，原本没有值的位置皆以NaN填充。
'''
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[1, 2, 3])

# 纵向"外"合并df1与df2
res = pd.concat([df1, df2], axis=0, join="outer", sort=False)
print(res)
#      a    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN
# 2  0.0  0.0  0.0  0.0  NaN
# 3  0.0  0.0  0.0  0.0  NaN
# 1  NaN  1.0  1.0  1.0  1.0
# 2  NaN  1.0  1.0  1.0  1.0
# 3  NaN  1.0  1.0  1.0  1.0

# 纵向"内"合并df1与df2
res = pd.concat([df1, df2], axis=0, join="inner")
print(res)
#      b    c    d
# 1  0.0  0.0  0.0
# 2  0.0  0.0  0.0
# 3  0.0  0.0  0.0
# 1  1.0  1.0  1.0
# 2  1.0  1.0  1.0
# 3  1.0  1.0  1.0

# 重置index
res = pd.concat([df1, df2], axis=0, join="inner", ignore_index=True)
print(res)

#      b    c    d
# 0  0.0  0.0  0.0
# 1  0.0  0.0  0.0
# 2  0.0  0.0  0.0
# 3  1.0  1.0  1.0
# 4  1.0  1.0  1.0
# 5  1.0  1.0  1.0


# join_axes(依照axes合并)
df3 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df4 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])

# 依照'df3.index'进行横向合并
res = pd.concat([df3, df4], axis=1, join_axes=[df3.index], sort=False)
print(res)
#      a    b    c    d    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
# 2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0

# 移除join_axes，打印结果
res = pd.concat([df3, df4], axis=1)
print(res)
#      a    b    c    d    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
# 2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 4  NaN  NaN  NaN  NaN  1.0  1.0  1.0  1.0

# append 添加数据
'''
append 只有纵向合并，没有横向合并
'''
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

# 将df2合并到df1的下面，以及重置index，并打印结果
res = df1.append(df2, ignore_index=True)
print(res)
#      a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  1.0  1.0  1.0
# 4  1.0  1.0  1.0  1.0
# 5  1.0  1.0  1.0  1.0

# 合并Series，将s1合并到df1, 以及重置index，并打印结果
res = df1.append(s1, ignore_index=True)
print(res)
#      a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  2.0  3.0  4.0



