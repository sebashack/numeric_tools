import numpy as np
from sympy import simplify
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication,
)


# Points are (xn,yn) tuples
def newton_interpolation(points):
    return interpolate(points, len(points) - 1)


def interpolate(points, k):
    assert k >= 0 and k <= len(points) - 1
    if k == 0:
        print(f"b0 = {points[k][1]}")
        return [points[k][1]]
    else:
        xn = points[k][0]
        bs = interpolate(points, k - 1)

        product = 1
        numerator = 0
        m = len(bs) - 1
        log_num = ""
        log_denom = ""
        for i, b in enumerate(bs):
            accum = 1
            log_num += f"b{i}"
            for j in range(0, i):
                log_denom += f"({xn} - {points[j][0]})"
                log_num += f"({xn} - {points[j][0]})"
                accum *= xn - points[j][0]

            if i == m:
                log_denom += f"({xn} - {points[k - 1][0]})"
                product = accum * (xn - points[k - 1][0])
            else:
                log_num += "-"
            numerator += b * accum

        yn = points[k][1]
        print(f"b{k} = [yn-{log_num}] / {log_denom}")

        bs.append((yn - numerator) / product)
    return bs


def print_bs(bs):
    for i in range(0, len(bs)):
        print(f"b{i} = {bs[i]}")


def gen_poly(points, bs):
    n = len(bs)
    poly = ""
    for i in range(0, n):
        prods = ""
        for j in range(0, i):
            xi = points[j][0]
            prods += f"(x - {xi})"

        if i == n - 1:
            poly += f"({bs[i]}{prods})"
        elif i == 0:
            poly += f"{bs[i]} + "
        else:
            poly += f"({bs[i]}{prods}) + "
    return poly


def simp_poly(poly):
    expr = parse_expr(
        poly, transformations=standard_transformations + (implicit_multiplication,)
    )
    return "{}".format(simplify(expr))


def newton_interpolation_by_diffs(points):
    n = len(points)
    table = np.zeros((n, n + 1), dtype=np.float64)

    for i, p in enumerate(points):
        table[i][0] = points[i][0]
        table[i][1] = points[i][1]

    bs = [table[0][1]]
    rows = table.shape[0]

    c = 0
    for j in range(2, n + 1):
        for i in range(j - 1, rows):
            num = table[i - 1][j - 1] - table[i][j - 1]
            denom = table[i - (1 + c)][j - (2 + c)] - table[i][j - (2 + c)]
            r = num / denom
            table[i][j] = r
            if j == i + 1:
                bs.append(r)

        c += 1

    return (table, bs)
