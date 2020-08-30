"""
迭代法解方程 Ax=b
输入x_0 A b times（迭代次数）
"""
import numpy as np


# -*- coding: utf-8 -*-

# Jacobi迭代法 输入系数矩阵A、值矩阵b、迭代次数n、误差c(以list模拟矩阵 行优先)

def Jacobi(A, b, x_0, n=100, c=0.0001):
    print('Jacobi Algorithm :')
    if len(A) == len(b):  # 若A和b长度相等则开始迭代 否则方程无解
        x = x_0  # 迭代初值
        count = 0  # 迭代次数计数
        while count < n:
            nx = []  # 保存单次迭代后的值的集合
            for i in range(len(x)):
                nxi = b[i][0]
                for j in range(len(A[i])):
                    if j != i:
                        nxi = nxi + (-A[i][j]) * x[j][0]
                nxi = nxi / A[i][i]
                nx.append([nxi])  # 迭代计算得到的下一个xi值
            lc = []  # 存储两次迭代结果之间的误差的集合
            for i in range(len(x)):
                lc.append(abs(x[i][0] - nx[i][0]))
            if max(lc) < c:
                print('End at ' + str(count) + ' because ' + str(max(lc)) + ' < c .')
                return x  # 当误差满足要求时 返回计算结果
            x = nx
            count = count + 1
        # return False #若达到设定的迭代结果仍不满足精度要求 则方程无解
        return x
    else:
        return False


def GS(A, b, x_0, n=100, c=0.0001):
    print('GS Algorithm :')
    A = np.array(A, np.float)
    size = A.shape[0]
    L = np.zeros_like(A)
    for i in range(size):
        for j in range(0, i+1):
            L[i, j] = A[i, j]
    print('L =\n', L)
    L_inv = np.linalg.inv(L)
    print('L_inv:\n', L_inv)
    print('(L-A) =\n', L-A)
    B = np.matmul(L_inv, (L-A))
    print('B =\n', B)
    b = np.matmul(L_inv, np.array(b).reshape(size, 1))
    print('b =\n', b)
    if len(A) == len(b):  # 若A和b长度相等则开始迭代 否则方程无解
        x = np.array(x_0).reshape(size, 1)  # 迭代初值
        count = 0  # 迭代次数计数
        while count < n:
            nx = np.matmul(B, x)+b
            diff = np.abs(nx-x).max()
            if diff < c:
                print('End at ' + str(count) + ' because ' + str(diff) + ' < c .')
                return x  # 当误差满足要求时 返回计算结果
            x = nx
            count = count + 1
        # return False #若达到设定的迭代结果仍不满足精度要求 则方程无解
        print(count)
        return x
    else:
        return False


def SOR(A, b, x_0, n=100, c=0.0001, omega=0.6):
    print('SOR Algorithm :')
    if len(A) == len(b):  # 若A和b长度相等则开始迭代 否则方程无解
        x = x_0  # 迭代初值
        count = 0  # 迭代次数计数
        while count < n:
            nx = []  # 保存单次迭代后的值的集合
            lc = []  # 存储两次迭代结果之间的误差的集合
            for i in range(len(x)):
                nxi = b[i][0]
                for j in range(len(A[i])):
                    if j < i:
                        nxi = nxi + (-A[i][j]) * nx[j][0]
                    if j > i:
                        nxi = nxi + (-A[i][j]) * x[j][0]
                nxi = nxi / A[i][i]
                nxi = omega * nxi + (1 - omega) * x[i][0]
                nx.append([nxi])  # 迭代计算得到的下一个xi值
                lc.append(abs(x[i][0] - nx[i][0]))
                # x[i][0]=nxi
            if max(lc) < c:
                print('End at ' + str(count) + ' because ' + str(max(lc)) + ' < c .')
                return x  # 当误差满足要求时 返回计算结果
            x = nx
            count = count + 1
        # return False #若达到设定的迭代结果仍不满足精度要求 则方程无解
        return x
    else:
        return False


# 调用 Jacobi(A,b,n=100,c=0.001) 示例
n = 100
c = 0.001  # 0为不适用该判据
A = [[10, 3, 1], [2, -10, 3], [1, 3, 10]]
# A = [
#     [2, 1, 0],
#     [-2, 4, 1],
#     [0, 2, 4]
# ]
b = [[14], [-5], [14]]
# x_0 = [[0], [0], [0]]
# print(Jacobi(A, b, x_0, n, c))
x_0 = [[0], [0], [0]]
print(GS(A, b, x_0, n, c))
# omega = 0.6
# x_0 = [[0], [0], [0]]
# print(SOR(A, b, x_0, n, c, omega))
