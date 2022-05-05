import numpy as np


# Points are (xn,yn) tuples
def newton_interpolation(points):
    return interpolate(points, len(points) - 1)


def interpolate(points, k):
    assert k >= 0 and k <= len(points) - 1
    if k == 0:
        return [points[k][1]]
    else:
        xn = points[k][0]
        bs = interpolate(points, k - 1)

        product = 1
        numerator = 0
        m = len(bs) - 1
        for i, b in enumerate(bs):
            accum = 1
            for j in range(0, i):
                accum *= xn - points[j][0]

            if i == m:
                product = accum * (xn - points[k - 1][0])
            numerator += b * accum

        yn = points[k][1]
        bs.append((yn - numerator) / product)
    return bs


def print_bs(bs):
    for i in range(0, len(bs)):
        print(f"b{i} = {bs[i]}")


def print_poly(points, bs):
    n = len(bs)
    for i in range(0, n):
        prods = ""
        for j in range(0, i):
            xi = points[j][0]
            prods += f"(x - {xi})"

        if i == n - 1:
            print(f"({bs[i]}*{prods})", end="\n")
        elif i == 0:
            print(f"{bs[i]}", end=" + ")
        else:
            print(f"({bs[i]}*{prods})", end=" + ")
