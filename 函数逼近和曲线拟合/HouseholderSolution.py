import numpy as np
from numpy import linalg as LA


def house(A):
    m, n = np.shape(A)
    W = np.zeros((m, n))
    R = A
    # householder procedure
    for k in range(n):
        # creat x, e, alpha
        x = A[k:m, k]
        e = np.zeros(len(x))
        e[0] = 1
        alpha = np.sign(x[0]) * LA.norm(x, 2)
        # creat u and v
        u = x + alpha * e
        v = u / LA.norm(u, 2)
        # creat R
        A[k:m, k:n] = A[k:m, k:n] - 2 * np.outer(v, np.dot(v.transpose(), A[k:m, k:n]))
        W[k:m, k] = v
    return W, R


def formQ(W):
    m, n = np.shape(W)
    Q = np.identity(m)
    for i in range(m):
        # x = Q[:,i]
        for k in range(n - 1, -1, -1):
            # x[k:m] = x[k:m] - 2 * np.outer(W[:,k],np.dot(W[:,k].transpose(),x[k:m]))
            Q[k:m, i] = Q[k:m, i] - 2 * np.dot(np.outer(W[k:m, k], W[k:m, k]), Q[k:m, i])
    # Q[k:m,i] = x[k:m]
    return Q


def valid(Q, R):
    return np.dot(Q, R)


def result(A_, b_):
    m, n = np.shape(A_)
    x = np.zeros(n)
    for i in range(1, n + 1):
        x[n - i] = b_[n - i][0]
        for j in range(1, i):
            x[n - i] -= x[n - j] * A_[n - i][n - j]
        x[n - i] = x[n - i] / A_[n - i][n - i]
    return x


A = np.array([[1, 0], [1, 1], [1, 4], [1, 9]], dtype='float64')  # matrix
b = np.array([[1], [1], [2], [3.5]])
print("A :")
print(A)
W, R = house(A)
print("W :")
print(W)
Q = formQ(W)
print("Q :")
print(Q)
print("R :")
print(R)
print("Q*R :")
print(valid(Q, R))
A = valid(Q, R)
A_ = valid(Q, A)
print("A_ :")
print(A_)
b_ = valid(Q, b)
print("b_ :")
print(b_)
resultx = result(R, b_)
print("x :")
print(resultx)
