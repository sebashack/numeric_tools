from collections import namedtuple
import numpy as np
from gaussian_elim_with_partial_pivot import solve_by_gaussian_elim_with_partial_pivot
from regressive_substitution import regressive_substitution

Si = namedtuple("Si", "ai bi xi")


def linear_splines(points):
    points_ = sorted(points)
    equations = []
    intervals = []
    for p0, p1 in zip(points_, points_[1:]):
        x0, f0 = p0
        x1, f1 = p1
        b = (f1 - f0) / (x1 - x0)
        intervals.append((x0, x1))
        equations.append(Si(f0, b, x0))
    return (equations, intervals)


def linear_eqs_strs(eqs, intervals):
    eq_ss = []
    for i, (eq, intv) in enumerate(zip(eqs, intervals)):
        s = f"s{i} = {eq.ai} + {eq.bi}(x - {eq.xi}), [{intv[0]},{intv[1]}]"
        eq_ss.append(s)

    return eq_ss


def quadratic_splines(points):
    points_ = sorted(points)
    num_intervals = len(points_) - 1
    dim = (num_intervals * 2) - 1
    hs = []
    zs = np.zeros(dim, dtype=np.float64)
    system = np.zeros((dim, dim), dtype=np.float64)

    col_shift = 0
    for i, (p0, p1) in enumerate(zip(points_, points_[1:])):
        h = p1[0] - p0[0]

        system[i][col_shift] = h
        if i == 0:
            col_shift += 1
        else:
            system[i][col_shift + 1] = np.power(h, 2)
            col_shift += 2

        hs.append(h)
        zs[i] = p1[1] - p0[1]

    col_shift = 0
    for i in range(num_intervals, dim):
        system[i][col_shift] = 1
        if i == num_intervals:
            system[i][col_shift + 1] = -1
            col_shift += 1
        else:
            system[i][col_shift + 1] = 2 * hs[i - num_intervals]
            system[i][col_shift + 2] = -1
            col_shift += 2

    ab = solve_by_gaussian_elim_with_partial_pivot(system, zs)
    sols = regressive_substitution(ab)

    return sols


def quadratic_eqs_strs(sols, points):
    i = 0
    k = 0
    n = len(sols)
    eqs = []

    while True:
        if k >= n:
            break

        ai = points[i][1]
        bi = sols[k]
        ci = None
        xi = points[i][0]
        if i == 0:
            ci = 0
            k += 1
        else:
            ci = sols[k + 1]
            k += 2

        if ci == 0:
            eqs.append(f"{ai} + {bi}(x - {xi})")
        else:
            eqs.append(f"{ai} + {bi}(x - {xi}) + {ci}(x - {xi})^2")
        i += 1

    return eqs


def print_quadratic_coefficients(points, sols):
    i = 0
    k = 0
    n = len(sols)
    while True:
        if k >= n:
            break

        print(f"a{i + 1} = {points[i][1]}")
        print(f"b{i + 1} = {sols[k]}")
        if i == 0:
            print(f"c{i + 1} = 0")
            k += 1
        else:
            print(f"c{i + 1} = {sols[k + 1]}")
            k += 2
        i += 1
