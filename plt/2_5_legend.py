import matplotlib.pyplot as plt
import numpy as np

'''
图例
https://morvanzhou.github.io/tutorials/data-manipulation/plt/2-5-lagend/
'''
x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
# set x limits
plt.xlim((-1, 2))
plt.ylim((-2, 3))
# set new sticks
new_sticks = np.linspace(-1, 2, 5)
plt.xticks(new_sticks)
# set tick labels
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# set line syles
l1, = plt.plot(x, y1, label='linear line')
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')
# 参数 loc='upper right' 表示图例将添加在图中的右上角.
plt.legend(loc='upper right')
# plt.show()


# 调整位置和名称
plt.legend(handles=[l1, l2], labels=['up', 'down'], loc='best')
plt.show()
'''
loc 参数：
 'best' : 0,          
 'upper right'  : 1,
 'upper left'   : 2,
 'lower left'   : 3,
 'lower right'  : 4,
 'right'        : 5,
 'center left'  : 6,
 'center right' : 7,
 'lower center' : 8,
 'upper center' : 9,
 'center'       : 10,
'''
