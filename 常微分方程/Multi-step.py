"""
初值问题的数值解法：多步法
"""
import numpy as np

alpha_mask = np.array([1, 0], np.bool)  # alpha 1~m 是否存在
beta_mask = np.array([1, 1], np.bool)  # beta  1~m 是否存在
mode = 0    # 0: 泰勒展开法；1: 单项式函数代入法(未实现……太难写了，还是手算吧ORZ)
given_params = True    # 是否给定alpha和beta
alpha = np.array([1, 0, 0, 0])  # 给定alpha时使用
beta = np.array([55/24, -59/24, 37/24, -9/24])  # 给定beta时使用


y = np.zeros(100)
y[0:4] = [0.4, 0.474638, 0.581387, 0.725066]   # y初值, m个
h = 0.1  # 步长
start = 1  # t初值
end = 2  # 要计算y(end)


def f(_t, _y):
    """ y'= f(t, y) """
    return pow(_t, 3) - _y / _t


# ------以上为可能需要修改的参数------

# 计算参数alpha和beta
if given_params:
    m = alpha.shape[0]
else:
    m = alpha_mask.shape[0]
if not given_params:
    params_mask = np.concatenate([alpha_mask, beta_mask])
    func_num = params_mask.sum()
    A0 = np.zeros([func_num, 2 * m])
    s = np.zeros(func_num)
    if mode == 0:
        for i in range(func_num):
            for j in range(m):
                A0[i][j] = pow(j+1, i) / np.math.factorial(i)
                if i != 0:
                    A0[i][m + j] = -pow(j+1, i - 1) / np.math.factorial(i - 1)
        s[0] = 1
    A1 = A0[:, params_mask]
    params = np.linalg.solve(A1, s)
    alpha = np.zeros(m)
    beta = np.zeros(m)
    alpha[alpha_mask] = params[:alpha_mask.sum()]
    beta[beta_mask] = params[alpha_mask.sum():]
print('alpha:', alpha)
print('beta:', beta)

# 多步法递推
eps = 1e-7
for i, t in enumerate(np.arange(start+m*h, end+eps, h)):
    y[i + m] = (alpha * y[i:i+m][::-1] + h * beta * f(np.arange(t-h, t-m*h-eps, -h), y[i:i+m][::-1])).sum()
    print('t = %f, y = %f' % (t, y[i + m]))
