#!/usr/bin/env python3
# encoding: utf-8
import numpy as np
'''
Numpy array 分割
Ref: https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/2-7-np-split/
'''

a = np.arange(12).reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# 纵向分割
print(np.split(a, 2, axis=1))
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2,  3],
#        [ 6,  7],
#        [10, 11]])]

# 横向分割
print(np.split(a, 3, axis=0))
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]

# 范例：错误的分割
# 范例的Array只有4列，只能等量对分，因此输入以上程序代码后Python就会报错。
# 横向、纵向均只能对等分
# print(np.split(a, 3, axis=1))
# array split does not result in an equal division

# 不等量的分割
# np.array_split()

print(np.array_split(a, 3, axis=1))
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2],
#        [ 6],
#        [10]]), array([[ 3],
#        [ 7],
#        [11]])]

# 其他的分割方式
print(np.vsplit(a, 3))  # 等于 print(np.split(a, 3, axis=0))
print(np.hsplit(a, 2))  # 等于 print(np.split(a, 2, axis=1))





