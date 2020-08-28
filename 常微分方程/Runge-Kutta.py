"""
初值问题的数值解法：Runge-Kutta
"""
import numpy as np


r = 4       # 级数，仅支持2、3、4
y = 0.4       # y初值，即y(start)
h = 0.1    # 步长
start = 1   # t初值
end = 2   # 要计算y(end)
lambda_params = np.array([   # 默认的2、3、4阶Runge-Kutta参数值
    [3, 3, 0, 0],   # 2阶
    [1, 4, 1, 0],   # 3阶
    [1, 2, 2, 1],   # 4阶
])


def f(_t, _y):
    """ y'= f(t, y) """
    return pow(_t, 3) - _y / _t

# ------以上为可能需要修改的参数------


for t in np.arange(start, end, h):
    print('t = %f, y = %f' % (t, y))
    k = np.zeros(4)
    k[0] = f(t, y)
    for i in range(r-2):
        k[i+1] = f(t + h/2, y + h/2 * k[i])
    k[r-1] = f(t + h, y + h * k[r-2])
    y += h * (k * lambda_params[r-2]).sum() / 6
print('t = %f, y = %f' % (end, y))
