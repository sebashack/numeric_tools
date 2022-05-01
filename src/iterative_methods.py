import numpy as np


# err_type = abs | rel | fx
def jacobi_method(a, b, init, tol, n, err_type="abs"):
    assert a.shape[0] == a.shape[1]
    assert a.shape[0] == len(b)
    assert len(init) == len(b)

    error = float("inf")

    xn = init
    i = 0
    print(f"{iter} | [x0,...,xn] | err_abs | err_rel")
    print(f"{i} | {xn} | err_abs=NA | err_rel=NA")
    while error > tol and i < n:
        x, abs_err, rel_err = next_iteration(a, b, xn)
        xn = x

        if err_type == "rel":
            error = abs_err
        else:
            error = rel_err

        i += 1
        print(f"{i} | {xn} | abs_err={abs_err} | rel_err={rel_err}")
    return xn


def next_iteration(a, b, prev_approx):
    n = a.shape[0]
    new_approx = np.zeros(n, dtype=np.float64)

    for i in range(0, n):
        d = a[i][i]
        accum = 0
        for j in range(0, n):
            if j != i:
                accum += a[i][j] * prev_approx[j]
        new_approx[i] = (b[i] - accum) / d

    errs = abs(new_approx - prev_approx)
    abs_err = max(errs)
    rel_err = max(errs / abs(new_approx))

    return (new_approx, abs_err, rel_err)
