"""
初值问题的数值解法：向后欧拉法 或 梯形法
！！！注意：第40行的[start-10, start+10]为每一步解的范围估计，如果题目中的解不在此范围内，需要修改！！！
"""
import numpy as np
from scipy.optimize import fsolve

mode = 0    # 0: 向后欧拉法；1: 梯形法
y = 1       # y初值，即y(start)
h = 0.025   # 步长
start = 0   # t初值
end = 0.15  # 要计算y(end)


def f(_t, _y):
    """ y'= f(t, y) """
    return -100 * _y


# ------以上为可能需要修改的参数------


def function(t_n, y_n):
    t_n1 = t_n + h

    def _func0(y_n1):
        return y_n1 - y_n - h * f(t_n1, y_n1)

    def _func1(y_n1):
        return y_n1 - y_n - 0.5 * h * (f(t_n, y_n) + f(t_n1, y_n1))

    if mode == 0:
        return _func0
    else:
        return _func1


for t in np.arange(start, end, h):
    print('t = %f, y = %f' % (t, y))
    y = fsolve(function(t, y), [start - 10, start + 10])[0]
print('t = %f, y = %f' % (end, y))
