import pandas as pd
import numpy as np
'''
Series的字符串表现形式为：索引在左边，值在右边。
由于我们没有为数据指定索引。于是会自动创建一个0到N-1（N为长度）的整数型索引。
'''
s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)
# 0     1.0
# 1     3.0
# 2     6.0
# 3     NaN
# 4    44.0
# 5     1.0
# dtype: float64


