"""
幂法求特征值
输入A u
"""
import numpy as np
# -*- coding: utf-8 -*-

def mifa(A,u,c=0.0001):
    print('SteepestDescent Algorithm :')
    if len(A) == len(u):  #若A和b长度相等则开始迭代 否则方程无解
        count = 0 #迭代次数计数
        u=np.array(u).reshape(-1)
        A=np.array(A)
        l1=0
        while count < 10000:
            v=A.dot(u)
            next_l1=np.max(np.abs(v))
            u=v/next_l1

            lc = abs(l1-next_l1)
            print('v =\n', v)
            print('lambda =\n', next_l1)
            print('u =\n', u)
            if np.max(lc) < c:
                print('End at '+str(count)+' because '+str(lc)+' < c .')
                return l1,u #当误差满足要求时 返回计算结果
            l1=next_l1
            count = count + 1
        #return False #若达到设定的迭代结果仍不满足精度要求 则方程无解
        return l1,u
    else:
        return False

def fanmifa(A,u,c=0.0001):
    print('SteepestDescent Algorithm :')
    if len(A) == len(u):  #若A和b长度相等则开始迭代 否则方程无解
        count = 0 #迭代次数计数
        u=np.array(u).reshape(-1)
        A=np.array(A)
        l1=0
        while count < 10000:
            v=np.linalg.inv(A).dot(u)
            next_l1=1/np.max(np.abs(v))
            u=v*next_l1

            lc = abs(l1-next_l1)
            if np.max(lc) < c:
                print('End at '+str(count)+' because '+str(lc)+' < c .')
                return l1,u #当误差满足要求时 返回计算结果
            l1=next_l1
            count = count + 1
        #return False #若达到设定的迭代结果仍不满足精度要求 则方程无解
        return l1,u
    else:
        return False

c=0.001 #0为不适用该判据
A = [[5,1/2,2],[1/2,6,3/2],[2,3/2,4]]
u = [1,1,1]
print(mifa(A,u,c))
