import numpy as np

'''
1. array：创建数组
2. dtype：指定数据类型
3. zeros：创建数据全为0
4. ones：创建数据全为1
5. empty：创建数据接近0
6. arrange：按指定范围创建数据
7. linspace：创建线段

'''

# 创建数组
a = np.array([2, 23, 4])
print(a)

# 指定数据类型 dtype
a = np.array([2, 23, 4], dtype=np.int)
print(a.dtype)
# int64

a = np.array([2, 23, 4], dtype=np.int32)
print(a.dtype)
# int32

a = np.array([2, 23, 4], dtype=np.float)
print(a.dtype)
# float64

a = np.array([2, 23, 4], dtype=np.float32)
print(a.dtype)
# float32

# 创建特定数据
a = np.array([[2, 23, 4], [2, 32, 4]])  # 2d 矩阵 2行3列
print(a)

# 创建全零数组
a = np.zeros((3, 4))  # 数据全为0，3行4列
print(a)

# 创建全一数组, 同时也能指定这些特定数据的 dtype:
a = np.ones((3, 4), dtype=np.int)
print(a)

# 创建全空数组, 其实每个值都是接近于零的数(3.6已全为零)
a = np.empty((3, 4))
print(a)

# 用 arange 创建连续数组:
a = np.arange(10, 20, 2)  # 10-19 的数据，2步长
print(a)

# 使用 reshape 改变数据的形状
a = np.arange(12).reshape((3, 4))  # 3行4列，0到11
print(a)

# 用 linspace 创建线段型数据:
a = np.linspace(1, 10, 20)  # 开始端1，结束端10，且分割成20个数据，生成线段
print(a)

# 同样也能进行 reshape 工作:
a = np.linspace(1, 10, 20).reshape((5, 4))  # 更改shape
print(a)


