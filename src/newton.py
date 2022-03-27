def newton(f, df, x0, tol, n, with_abs_err=True):
    x = x0
    fx = f(x)
    dfx = df(x)
    i = 0

    abs_err = tol + 1
    rel_err = abs_err
    error = abs_err

    while fx != 0 and error > tol and dfx != 0 and i < n:
        print(f"{i} -- f({x}) = {fx} -- abs_err = {abs_err} -- rel_err = {rel_err}")
        xn = x - (fx / dfx)
        fx = f(xn)
        dfx = df(xn)

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
        print(f"{i} -- f({x}) = {fx} -- asb_err = {abs_err} -- rel_err = {rel_err}")
    elif dfx == 0:
        print("possibly a multiple root")
    else:
        print(f"{i} -- Failed")
