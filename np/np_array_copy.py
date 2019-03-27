import numpy as np
'''
Numpy copy & deep copy
Ref: https://morvanzhou.github.io/tutorials/data-manipulation/np-pd/2-8-np-copy/
'''

# = 的赋值方式会带有关联性
a = np.arange(4)
b = a
c = a
d = b

a[0] = 11
print(a)
print(d[0])
print(b is a)  # True
print(c is a)  # True
print(d is a)  # True

# 同时更改d的值，a、b、c也会改变
d[1:3] = [22, 33]
print(a)  # [11 22 33  3]
print(b)  # [11 22 33  3]
print(c)  # [11 22 33  3]

# copy()的赋值没有关联性

b = a.copy()  # deep copy
print(b)  # [11 22 33  3]
a[3] = 44
print(a)  # [11 22 33 44]
print(b)  # [11 22 33  3]





