import numpy as np

'''
ref: https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/2-5-np-indexing/
'''

# 一维索引
a = np.arange(3, 15)
print(a[3])  # 6

a = np.arange(3, 15).reshape(3, 4)
print(a[2])  # [11 12 13 14]
# 二维索引
print(a[2][0])  # 11
print(a[2, 0])  # 11

print(a[2, 0:3])  # [11 12 13]

# 逐行遍历
for row in a:
    print(row)
# [3 4 5 6]
# [ 7  8  9 10]
# [11 12 13 14]

# 逐列遍历
for column in a.T:
    print(column)
# [ 3  7 11]
# [ 4  8 12]
# [ 5  9 13]
# [ 6 10 14]

# 逐个遍历，需要转成一维数组
print(a.flatten())

for item in a.flat:
    print(item)



