# err_type = abs | rel | fx
def fixed_point(f, g, x0, tol, n, err_type="abs"):
    x = x0
    fx = f(x)
    i = 0

    abs_err = float("inf")
    rel_err = float("inf")
    error = float("inf")

    if err_type == "fx":
        error = abs(fx)

    while fx != 0 and error > tol and i < n:
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

    if fx == 0 or error < tol:
        return x
    else:
        return None
