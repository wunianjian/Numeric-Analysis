"""
迭代法解方程 Ax=b
输入x_0 A b times（迭代次数）
"""
import numpy as np
# -*- coding: utf-8 -*-
 
#Jacobi迭代法 输入系数矩阵A、值矩阵b、迭代次数n、误差c(以list模拟矩阵 行优先)
 
def Jacobi(A,b,x_0,n=100,c=0.0001):
    if len(A) == len(b):  #若A和b长度相等则开始迭代 否则方程无解
        x = x_0 #迭代初值
        count = 0 #迭代次数计数
        while count < n:
            nx = [] #保存单次迭代后的值的集合
            for i in range(len(x)):
                nxi = b[i][0]
                for j in range(len(A[i])):
                    if j!=i:
                        nxi = nxi+(-A[i][j])*x[j][0]
                nxi = nxi/A[i][i]
                nx.append([nxi]) #迭代计算得到的下一个xi值
            lc = [] #存储两次迭代结果之间的误差的集合
            for i in range(len(x)):
                lc.append(abs(x[i][0]-nx[i][0]))
            if max(lc) < c:
                return nx #当误差满足要求时 返回计算结果
            x = nx
            count = count + 1
        #return False #若达到设定的迭代结果仍不满足精度要求 则方程无解
        return x
    else:
        return False
 
#调用 Jacobi(A,b,n=100,c=0.001) 示例
n=5
c=0 #0为不适用该判据
A = [[8,-3,2],[4,11,-1],[6,3,12]]
b = [[20],[33],[36]]
x_0 = [[0],[0],[0]]
print(Jacobi(A,b,x_0,n,c))
