"""
牛顿插值法。输入x1-xn,y1-yn,求多项式
"""
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 1, 4])

# ------以上为可能需要修改的参数------

n = x.shape[0]
f_diff = np.zeros([n, n])
f_diff[0, :] = y
for i in range(1, n):
    for j in range(i, n):
        f_diff[i, j] = (f_diff[i-1, j] - f_diff[i-1, j-1]) / (x[j] - x[j-i])
for i in range(n):
    print(f_diff[i, i], end='')
    for j in range(i):
        print('(x-({}))'.format(x[j]), end='')
    print()
