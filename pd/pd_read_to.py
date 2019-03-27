import pandas as pd

'''
Pandas 导入导出
Ref: https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/3-5-pd-to/
Ref: http://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
'''

# 读取csv
data = pd.read_csv('student.csv')
# print(data)

# 保存为pickle
data.to_pickle('student.pickle')
