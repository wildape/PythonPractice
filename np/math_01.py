import numpy as np

'''
Numpy 基础运算1
ref: https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/2-3-np-math1/
'''

a = np.array([10, 20, 30, 40])  # array([10, 20, 30, 40])
b = np.arange(4)  # array([0, 1, 2, 3])

c = a - b  # [10 19 28 37]
print(c)
c = a + b  # array([10, 21, 32, 43])
print(c)
c = a * b  # array([  0,  20,  60, 120])
print(c)
# 次方
c = b ** 2
print(c)  # [0 1 4 9]

# 函数运算
c = 10 * np.sin(a)
print(c)

# 逻辑判断
print(b < 3)  # [ True  True  True False]

a = np.array([[1, 1], [0, 1]])
b = np.arange(4).reshape((2, 2))

print(a)
# [[1 1]
#  [0 1]]
print(b)
# [[0 1]
#  [2 3]]

# 标准矩阵乘法
c_dot = np.dot(a, b)
print(c_dot)
# [[2 4]
#  [2 3]]

# 除此之外还有另外的一种关于dot的表示方法，即：
c_dot_2 = a.dot(b)
print(c_dot_2)
# [[2 4]
#  [2 3]]


