#!/usr/bin/env python3
# encoding: utf-8
import numpy as np
import pandas as pd

'''
DataFrame是一个表格型的数据结构，它包含有一组有序的列，
每列可以是不同的值类型（数值，字符串，布尔值等）。
DataFrame既有行索引也有列索引， 它可以被看做由Series组成的大字典。
'''
dates = pd.date_range('20190101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])

print(df)
#                    a         b         c         d
# 2019-01-01  2.393820 -0.051827  0.263300 -0.549029
# 2019-01-02 -1.338768 -0.994082 -1.898015 -1.109404
# 2019-01-03 -0.978043  1.051412 -1.063899 -1.989350
# 2019-01-04  1.213606  0.212856 -1.925941 -0.028932
# 2019-01-05 -0.732194  0.552476  0.323306 -2.725010
# 2019-01-06  0.744884 -0.102437  0.906533  0.784940

print(df['b'])
# 2019-01-01   -0.051827
# 2019-01-02   -0.994082
# 2019-01-03    1.051412
# 2019-01-04    0.212856
# 2019-01-05    0.552476
# 2019-01-06   -0.102437
# Freq: D, Name: b, dtype: float64

# 创建一组没有给定行标签和列标签的数据 df1:
df1 = pd.DataFrame(np.arange(12).reshape(3, 4))
print(df1)
#    0  1   2   3
# 0  0  1   2   3
# 1  4  5   6   7
# 2  8  9  10  11
# 这样,他就会采取默认的从0开始 index.

df2 = pd.DataFrame({'A': 1,
                    'B': pd.Timestamp('20190101'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'
                    })
print(df2)
#    A          B    C  D      E    F
# 0  1 2019-01-01  1.0  3   test  foo
# 1  1 2019-01-01  1.0  3  train  foo
# 2  1 2019-01-01  1.0  3   test  foo
# 3  1 2019-01-01  1.0  3  train  foo

# 查看数据中的类型
print(df2.dtypes)
# A             int64
# B    datetime64[ns]
# C           float32
# D             int32
# E          category
# F            object
# dtype: object

# 查看列的序号
print(df2.index)
# Int64Index([0, 1, 2, 3], dtype='int64')

# 每种数据的名称
print(df2.columns)
# Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')

# df2的值
print(df2.values)
# [[1 Timestamp('2019-01-01 00:00:00') 1.0 3 'test' 'foo']
#  [1 Timestamp('2019-01-01 00:00:00') 1.0 3 'train' 'foo']
#  [1 Timestamp('2019-01-01 00:00:00') 1.0 3 'test' 'foo']
#  [1 Timestamp('2019-01-01 00:00:00') 1.0 3 'train' 'foo']]

# 数据总结 describe()
print(df2.describe())
#          A    C    D
# count  4.0  4.0  4.0
# mean   1.0  1.0  3.0
# std    0.0  0.0  0.0
# min    1.0  1.0  3.0
# 25%    1.0  1.0  3.0
# 50%    1.0  1.0  3.0
# 75%    1.0  1.0  3.0
# max    1.0  1.0  3.0

# 翻转数据
print(df2.T)

# 对数据的index进行排序并输出
print(df2.sort_index(axis=1, ascending=False))
#      F      E  D    C          B  A
# 0  foo   test  3  1.0 2019-01-01  1
# 1  foo  train  3  1.0 2019-01-01  1
# 2  foo   test  3  1.0 2019-01-01  1
# 3  foo  train  3  1.0 2019-01-01  1

# 对数据的值排序输出
print(df2.sort_values(by='B'))
#    A          B    C  D      E    F
# 0  1 2019-01-01  1.0  3   test  foo
# 1  1 2019-01-01  1.0  3  train  foo
# 2  1 2019-01-01  1.0  3   test  foo
# 3  1 2019-01-01  1.0  3  train  foo




