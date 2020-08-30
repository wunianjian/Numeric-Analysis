import numpy as np
from numpy import linalg as LA

A = np.array([[1, 0],[1,1],[1,2],[1,3]],dtype='float64')#matrix
b = np.array([[1],[1],[2],[0]])

print("A :")
print(A)
print("AT:")
print(A.T)
ATA = np.dot(A.T,A)
print("ATA:")
print(ATA)
ATb = np.dot(A.T,b)
print("ATb:")
print(ATb)
x = np.dot(np.linalg.inv(ATA),ATb)
print("x:")
print(x)