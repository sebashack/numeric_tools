def fixed_point(f, g, dg, x0, tol, n, err_type="abs"):
    x = x0
    fx = f(x)
    i = 0

    abs_err = float("inf")
    rel_err = float("inf")
    error = float("inf")

    dg_ = None
    if dg is None:

        def dg_(x):
            return "NA"

    else:
        dg_ = dg

    if err_type == "fx":
        error = abs(fx)

    while fx != 0 and error > tol and i < n:
        dgx = dg_(x)

        print(
            f"{i} -- f({x}) = {fx} -- dg(x) = {dgx} -- abs_err = {abs_err} -- rel_err = {rel_err}"
        )

        xn = g(x)
        fx = f(xn)

        abs_err = abs(xn - x)
        rel_err = abs_err / abs(xn)

        if err_type == "fx":
            error = abs(fx)
        elif err_type == "rel":
            error = rel_err
        else:
            error = abs_err

        x = xn
        i = i + 1

    if fx == 0:
        print(f"{i} -- f({x}) = {fx} -- dg(x) = {dg_(x)} -- exact root")
    elif error < tol:
        print(
            f"{i} -- f({x}) = {fx} -- dg(x) = {dg_(x)} -- err = {abs_err} -- rel_err = {rel_err}"
        )
    else:
        print(f"{i} -- Failed")
