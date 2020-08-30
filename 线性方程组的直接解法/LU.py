"""
LU分解：高斯消去法，支持采用部分选主元技术
"""
import numpy as np

A = np.array([
    [2, 1, 0],
    [-2, 4, 1],
    [0, 2, 4],
], np.float)
part_select_pivot = False    # 是否采用部分选主元

# ------以上为可能需要修改的参数------

n = A.shape[0]
p = np.eye(n)
for k in range(n-1):
    if part_select_pivot:
        s = A[k:].argmax(0)[k] + k
        if s != k:
            A[[k, s]] = A[[s, k]]
            p[[k, s]] = p[[s, k]]
    elif A[k, k] == 0:
        break
    for i in range(k+1, n):
        A[i, k] /= A[k, k]
        for j in range(k+1, n):
            A[i, j] -= A[i, k] * A[k, j]
print('A =\n', A)
print('P =\n', p)
