import math


def maximum_dg(interval, dx, derivative):
    d = abs(interval[1] - interval[0])
    n = math.ceil(d / dx)

    x = interval[0] + 0.00001
    dmax = abs(derivative(x))

    for i in range(1, n):
        x = x + dx

        if x >= interval[1]:
            break

        v = abs(derivative(x))
        dmax = max(dmax, v)

    return dmax
