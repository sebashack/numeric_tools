import math


def fixed_point(f, g, x0, tol, n, with_abs_err=True):
    x = x0
    fx = f(x)
    i = 0

    abs_err = tol + 1
    rel_err = abs_err
    error = abs_err

    while fx != 0 and error > tol and i < n:
        # print(f"{i} -- f({x}) = {fx} -- abs_err = {abs_err} -- rel_err = {rel_err}")

        xn = g(x)
        fx = f(xn)

        abs_err = abs(xn - x)
        rel_err = abs_err / abs(xn)

        if with_abs_err:
            error = abs_err
        else:
            error = rel_err

        x = xn
        i = i + 1

    if fx == 0:
        print(f"{i} -- f({x}) = {fx} -- exact root")
    elif error < tol:
        print(f"{i} -- f({x}) = {fx} -- err = {abs_err} -- rel_err = {rel_err}")
    else:
        print(f"{i} -- Failed")
