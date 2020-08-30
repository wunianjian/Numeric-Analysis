import math


def Newton_Cotes(n, a, b, f):
    if n == 1:
        return (b - a) / 2 * (f(a) + f(b))
    elif n == 2:
        return (b - a) / 6 * (f(a) + 4 * f(a / 2 + b / 2) + f(b))
    elif n == 4:
        return (b - a) / 90 * (7 * f(a) + 32 * f(a + (b - a) / 4) + 12 * f(a + (b - a) / 2) + 32 * f(a + 3 * (b - a) / 4) + 7 * f(b))


def Composite_Quad(n, a, b, f, mode='simpson'):
    h = (b - a) / n
    res = 0
    if mode == 'trapezium':
        for i in range(n + 1):
            res += h * f(a + i * h)

        return res - h * f(a) / 2 - h * f(b) / 2

    elif mode == 'simpson':
        for i in range(n):
            res += h / 6 * (f(a + i * h) + 4 * f(a + i * h + h / 2) + f(a + i * h + h))
        return res


def Romberg(n, a, b, f):
    T_0_n1 = Composite_Quad(n * 2, a, b, f, 'trapezium')
    T_0_n = Composite_Quad(n, a, b, f, 'trapezium')
    print('T_0_n1 =', T_0_n1)
    print('T_0_n =', T_0_n)
    return (4 * T_0_n1 - T_0_n) / 3


def Gauss(n, a, b, f):
    xk = {0: [0],
          1: [-0.5773503, 0.5773503],
          2: [-0.7745967, 0.7745967, 0],
          3: [-0.8611363, 0.8611363, -0.3399810, 0.3399810],
          4: [-0.9061798, 0.9061798, -0.5384693, 0.5384693, 0],
          5: [-0.9324695, 0.9324695, -0.6612094, 0.6612094, -0.2386192, 0.2386192]}
    Ak = {0: [2],
          1: [1, 1],
          2: [0.5555556, 0.5555556, 0.8888889],
          3: [0.3478548, 0.3478548, 0.6521452, 0.6521452],
          4: [0.2369269, 0.2369269, 0.4786287, 0.4786287, 0.5688889],
          5: [0.1713245, 0.1713245, 0.3607616, 0.3607616, 0.4679139, 0.4679139]}
    xk = xk[n]
    Ak = Ak[n]
    p = (b - a) / 2
    res = 0
    for i in range(n + 1):
        print('i = %d, x = %f, A = %f' % (i, a + (b - a) / 2 * (1 + xk[i]), Ak[i]))
        res += Ak[i] * f(a + (b - a) / 2 * (1 + xk[i]))

    return p * res


def func(x):
    return 1 / (x*x+2)


eps = 1e-10
print(Gauss(1, -2, 2, func))
# print('res =', Romberg(1, -1, 1, func))
# print(Composite_Quad(4, 0+eps, 1, func))
# print(Newton_Cotes(4, 0+eps, 1, func))
