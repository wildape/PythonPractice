import numpy as np
import pandas as pd

'''
Pandas 处理丢失数据
Ref: https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/3-4-pd-nan/
'''

# 创建含NaN的矩阵
'''
有时候我们导入或处理数据, 
会产生一些空的或者是 NaN 数据,
如何删除或者是填补这些 NaN 数据就是我们今天所要提到的内容.
'''
dates = pd.date_range('20190101', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)
#              A     B     C   D
# 2019-01-01   0   NaN   2.0   3
# 2019-01-02   4   5.0   NaN   7
# 2019-01-03   8   9.0  10.0  11
# 2019-01-04  12  13.0  14.0  15
# 2019-01-05  16  17.0  18.0  19
# 2019-01-06  20  21.0  22.0  23

# pd.dropna()
'''
如果想直接去掉有 NaN 的行或列, 可以使用 dropna
此处会返回一个新的DataFrame，之前的DataFrame不会改变
'''
# df = df.dropna(
#     axis=0,    # 0: 对行进行操作；1: 对列进行操作
#     how='any'  # 'any': 只要存在NaN就drop掉；'all': 必须全部是NaN才drop
# )

print(df.dropna(axis=0, how='any'))
#              A     B     C   D
# 2019-01-03   8   9.0  10.0  11
# 2019-01-04  12  13.0  14.0  15
# 2019-01-05  16  17.0  18.0  19
# 2019-01-06  20  21.0  22.0  23

# pd.fillna()
'''
如果是将 NaN 的值用其他值代替, 比如代替成 0:
此处会返回一个新的DataFrame，之前的DataFrame不会改变
'''
print(df.fillna(value=0))
#              A     B     C   D
# 2019-01-01   0   0.0   2.0   3
# 2019-01-02   4   5.0   0.0   7
# 2019-01-03   8   9.0  10.0  11
# 2019-01-04  12  13.0  14.0  15
# 2019-01-05  16  17.0  18.0  19
# 2019-01-06  20  21.0  22.0  23

# pd.isna()
print(df.isna())
#                 A      B      C      D
# 2019-01-01  False   True  False  False
# 2019-01-02  False  False   True  False
# 2019-01-03  False  False  False  False
# 2019-01-04  False  False  False  False
# 2019-01-05  False  False  False  False
# 2019-01-06  False  False  False  False

# 检测在数据中是否存在 NaN, 如果存在就返回 True:
print(np.any(df.isnull()) == True)


