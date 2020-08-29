"""
迭代法解方程 Ax=b
输入x_0 A b times（迭代次数）
"""
import numpy as np
# -*- coding: utf-8 -*-
 
#SteepestDescent迭代法 输入系数矩阵A、值矩阵b、迭代次数n、误差c(以list模拟矩阵 行优先)

def SteepestDescent(A,b,x_0,n=100,c=0.0001):
    print('SteepestDescent Algorithm :')
    if len(A) == len(b):  #若A和b长度相等则开始迭代 否则方程无解
        x = x_0 #迭代初值
        count = 0 #迭代次数计数
        x=np.array(x).reshape(-1)
        A=np.array(A)
        b=np.array(b).reshape(-1)
        r=b-A.dot(x)
        #print(x,A,b,r)
        while count < n:
            alpha=r.T.dot(r)/(r.T.dot(A.dot(r)))
            next_x=x+alpha*r
            r=r-alpha*A.dot(r)

            lc = np.abs(x-next_x)
            if np.max(lc) < c:
                print('End at '+str(count)+' because '+str(max(lc))+' < c .')
                return x #当误差满足要求时 返回计算结果
            x = next_x
            count = count + 1
        #return False #若达到设定的迭代结果仍不满足精度要求 则方程无解
        return x
    else:
        return False

def CG(A,b,x_0,n=100,c=0.0001):
    print('CG Algorithm :')
    if len(A) == len(b):  #若A和b长度相等则开始迭代 否则方程无解
        x = x_0 #迭代初值
        count = 0 #迭代次数计数
        x=np.array(x).reshape(-1)
        A=np.array(A)
        b=np.array(b).reshape(-1)
        r=b-A.dot(x)
        p=r
        while count < n:
            alpha=r.T.dot(r)/(p.T.dot(A.dot(p)))
            next_x=x+alpha*p
            r2=r
            r=r-alpha*A.dot(p)
            beta=r.T.dot(r)/r2.T.dot(r2)
            p=r+beta*p
            lc = np.abs(x-next_x)
            if np.max(lc) < c:
                print('End at '+str(count)+' because '+str(max(lc))+' < c .')
                return x #当误差满足要求时 返回计算结果
            x = next_x
            count = count + 1
        #return False #若达到设定的迭代结果仍不满足精度要求 则方程无解
        return x
    else:
        return False

#调用 Jacobi(A,b,n=100,c=0.001) 示例
n=100
c=0.001 #0为不适用该判据
A = [[3,2],[2,6]]
b = [2,-8]
x_0 = [-2,-2]
print(SteepestDescent(A,b,x_0,n,c))
x_0 = [-2,-2]
print(CG(A,b,x_0,n,c))
