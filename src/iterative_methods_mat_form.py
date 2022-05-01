import numpy as np


def jacobi_method_mat(a, b, init, tol, iters, err_type="abs"):
    assert a.shape[0] == a.shape[1]
    assert a.shape[0] == len(b)
    assert len(init) == len(b)

    t, c = tc_jacobi(a, b)
    error = float("inf")
    xn = init
    i = 0

    print("iter | [x0,...,xn] | err_abs | err_rel")
    print(f"{i} | {xn} | err_abs=NA | err_rel=NA")
    while error > tol and i < iters:
        x = t.dot(xn) + c

        errs = abs(x - xn)
        abs_err = max(errs)
        rel_err = max(errs / abs(x))

        xn = x

        if err_type == "rel":
            error = rel_err
        else:
            error = abs_err

        i += 1
        print(f"{i} | {xn} | abs_err={abs_err} | rel_err={rel_err}")

    return xn


def tc_jacobi(a, b):
    assert a.shape[0] == a.shape[1]
    assert a.shape[0] == len(b)

    n = a.shape[0]
    d = np.eye(n) * a

    lo = np.negative(np.triu(a))
    np.fill_diagonal(lo, 0)

    up = np.negative(np.tril(a))
    np.fill_diagonal(up, 0)

    dinv = np.linalg.inv(d)
    t = dinv.dot(lo + up)
    c = dinv.dot(b)

    return (t, c)


def seidel_method_mat(a, b, init, tol, iters, err_type="abs"):
    assert a.shape[0] == a.shape[1]
    assert a.shape[0] == len(b)
    assert len(init) == len(b)

    t, c = tc_seidel(a, b)
    error = float("inf")
    xn = init
    i = 0

    print("iter | [x0,...,xn] | err_abs | err_rel")
    print(f"{i} | {xn} | err_abs=NA | err_rel=NA")
    while error > tol and i < iters:
        x = t.dot(xn) + c

        errs = abs(x - xn)
        abs_err = max(errs)
        rel_err = max(errs / abs(x))

        xn = x

        if err_type == "rel":
            error = rel_err
        else:
            error = abs_err

        i += 1
        print(f"{i} | {xn} | abs_err={abs_err} | rel_err={rel_err}")

    return xn


def tc_seidel(a, b):
    assert a.shape[0] == a.shape[1]
    assert a.shape[0] == len(b)

    n = a.shape[0]
    d = np.eye(n) * a

    lo = np.negative(np.triu(a))
    np.fill_diagonal(lo, 0)

    up = np.negative(np.tril(a))
    np.fill_diagonal(up, 0)

    dlinv = np.linalg.inv(d - lo)
    t = dlinv.dot(up)
    c = dlinv.dot(b)

    return (t, c)


def spectral_radius(a):
    assert a.shape[0] == a.shape[1]
    return np.max((np.absolute(np.linalg.eigvals(a))))
