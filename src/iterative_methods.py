import numpy as np


# err_type = abs | rel | fx
def jacobi_method(a, b, init, tol, n, err_type="abs"):
    assert a.shape[0] == a.shape[1]
    assert a.shape[0] == len(b)
    assert len(init) == len(b)

    error = float("inf")

    xn = init
    i = 0

    print("iter | [x0,...,xn] | err_abs | err_rel")
    print(f"{i} | {xn} | err_abs=NA | err_rel=NA")
    while error > tol and i < n:
        x, abs_err, rel_err = next_jacobi_iteration(a, b, xn)
        xn = x

        if err_type == "rel":
            error = rel_err
        else:
            error = abs_err

        i += 1
        print(f"{i} | {xn} | abs_err={abs_err} | rel_err={rel_err}")
    return xn


def next_jacobi_iteration(a, b, prev_x):
    n = a.shape[0]
    x = np.zeros(n, dtype=np.float64)

    for i in range(0, n):
        d = a[i][i]
        accum = 0
        for j in range(0, n):
            if j != i:
                accum += a[i][j] * prev_x[j]
        x[i] = (b[i] - accum) / d

    errs = abs(x - prev_x)
    abs_err = max(errs)
    rel_err = max(errs / abs(x))

    return (x, abs_err, rel_err)


# err_type = abs | rel | fx
def seidel_method(a, b, init, tol, n, err_type="abs"):
    assert a.shape[0] == a.shape[1]
    assert a.shape[0] == len(b)
    assert len(init) == len(b)

    error = float("inf")
    xn = init
    i = 0

    print("iter | [x0,...,xn] | err_abs | err_rel")
    print(f"{i} | {xn} | err_abs=NA | err_rel=NA")
    while error > tol and i < n:
        x, abs_err, rel_err = next_seidel_iteration(a, b, xn)
        xn = x

        if err_type == "rel":
            error = rel_err
        else:
            error = abs_err

        i += 1
        print(f"{i} | {xn} | abs_err={abs_err} | rel_err={rel_err}")
    return xn


def next_seidel_iteration(a, b, prev_x):
    n = a.shape[0]
    x = np.zeros(n, dtype=np.float64)

    k = -1
    for i in range(0, n):
        d = a[i][i]
        accum = 0
        c = 0
        for j in range(0, n):
            if j != i:
                if c <= k:
                    accum += a[i][j] * x[c]
                    c += 1
                else:
                    accum += a[i][j] * prev_x[j]
        x[i] = (b[i] - accum) / d
        k += 1

    errs = abs(x - prev_x)
    abs_err = max(errs)
    rel_err = max(errs / abs(x))

    return (x, abs_err, rel_err)
