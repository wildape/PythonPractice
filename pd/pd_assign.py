#!/usr/bin/env python3
# encoding: utf-8
import numpy as np
import pandas as pd

'''
Pandas 设置值
Ref: https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/3-3-pd-assign/
'''
dates = pd.date_range('20190101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
#              A   B   C   D
# 2019-01-01   0   1   2   3
# 2019-01-02   4   5   6   7
# 2019-01-03   8   9  10  11
# 2019-01-04  12  13  14  15
# 2019-01-05  16  17  18  19
# 2019-01-06  20  21  22  23

# 根据位置设置loc和iloc
'''
我们可以利用索引或者标签确定需要修改值的位置。
'''
df.iloc[2, 2] = 1111
print(df)
#              A   B     C   D
# 2019-01-01   0   1     2   3
# 2019-01-02   4   5     6   7
# 2019-01-03   8   9  1111  11
# 2019-01-04  12  13    14  15
# 2019-01-05  16  17    18  19
# 2019-01-06  20  21    22  23

# 根据条件设置
'''
如果现在的判断条件是这样, 我们想要更改B中的数, 
而更改的位置是取决于 A 的. 对于A大于4的位置. 
更改B在相应位置上的数为0.
'''
df.B[df.A > 4] = 0
print(df)
#              A  B     C   D
# 2019-01-01   0  1     2   3
# 2019-01-02   4  5     6   7
# 2019-01-03   8  0  1111  11
# 2019-01-04  12  0    14  15
# 2019-01-05  16  0    18  19
# 2019-01-06  20  0    22  23


# 按行或列设置
'''
如果对整列做批处理, 加上一列 ‘F’, 并将 F 列全改为 NaN, 如下:
'''
df['F'] = np.nan
print(df)
#              A  B     C   D   F
# 2019-01-01   0  1     2   3 NaN
# 2019-01-02   4  5     6   7 NaN
# 2019-01-03   8  0  1111  11 NaN
# 2019-01-04  12  0    14  15 NaN
# 2019-01-05  16  0    18  19 NaN
# 2019-01-06  20  0    22  23 NaN

# 添加数据
'''
用上面的方法也可以加上 Series 序列（但是长度必须对齐）。
'''
df['E'] = pd.Series(np.arange(6), index=pd.date_range('20190101', periods=6))
print(df)
#              A  B     C   D   F  E
# 2019-01-01   0  1     2   3 NaN  0
# 2019-01-02   4  5     6   7 NaN  1
# 2019-01-03   8  0  1111  11 NaN  2
# 2019-01-04  12  0    14  15 NaN  3
# 2019-01-05  16  0    18  19 NaN  4
# 2019-01-06  20  0    22  23 NaN  5
