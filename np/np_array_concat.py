import numpy as np

'''
array合并
Ref: https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/2-6-np-concat/
'''
a = np.array([1, 1, 1])
b = np.array([2, 2, 2])

# np.vstack() 竖直合并
print(np.vstack((a, b)))  # vertical stack
# [[1 1 1]
#  [2 2 2]]

c = np.vstack((a, b))
print(a.shape, c.shape)

# np.hstack() 水平合并
d = np.hstack((a, b))
print(d)
print(a.shape, d.shape)

# np.newaxis() 转置
print(a[np.newaxis, :])  # [[1 1 1]] 一行 三列的矩阵
print(a[np.newaxis, :].shape)  #(1, 3)


print(a[:, np.newaxis])  # 三行一列的矩阵
# [[1]
#  [1]
#  [1]]
print(a[:, np.newaxis].shape)  # (3, 1)

A = np.array([1, 1, 1])[:, np.newaxis]
B = np.array([2, 2, 2])[:, np.newaxis]

C = np.vstack((A, B))  # vertical stack
D = np.hstack((A, B))  # horizontal stack

print(D)
"""
[[1 2]
[1 2]
[1 2]]
"""

print(A.shape, D.shape)
# (3,1) (3,2)

# np.concatenate()

C = np.concatenate((A, B, B, A), axis=0)
print(C)
# [[1]
#  [1]
#  [1]
#  [2]
#  [2]
#  [2]
#  [2]
#  [2]
#  [2]
#  [1]
#  [1]
#  [1]]

D = np.concatenate((A, B, B, A), axis=1)
print(D)
# [[1 2 2 1]
#  [1 2 2 1]
#  [1 2 2 1]]





