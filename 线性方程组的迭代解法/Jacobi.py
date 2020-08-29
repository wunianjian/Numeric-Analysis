"""
初值问题的数值解法：欧拉法
"""
import numpy as np

y = 1       # y初值，即y(start)
h = 0.05    # 步长
start = 0   # t初值
end = 0.5   # 要计算y(end)


def f(_t, _y):
    """ y'= f(t, y) """
    return _t - _y + 1

# ------以上为可能需要修改的参数------


for t in np.arange(start, end, h):
    print('t = %f, y = %f' % (t, y))
    y += h * f(t, y)
print('t = %f, y = %f' % (end, y))
