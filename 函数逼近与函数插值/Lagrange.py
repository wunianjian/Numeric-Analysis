"""
拉格朗日插值法。输入x1-xn,y1-yn,xt,求yt
"""
import numpy as np

x = np.array([1, 2, 3, 0])
y = np.array([2, 9, 28, 1])
xt = 4

# ------以上为可能需要修改的参数------

n = x.shape[0]
yt = 0
for i in range(n):
    temp = 1
    for j in range(n):
        if i != j:
            temp *= (xt - x[j]) / (x[i] - x[j])
    yt += temp * y[i]
print('yt =', yt)
