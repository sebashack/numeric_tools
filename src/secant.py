def secant(f, interval, tol, n, with_abs_err=True):
    x0 = interval[0]
    x1 = interval[1]
    assert x1 > x0

    fx0 = f(x0)
    i = 0

    if fx0 == 0:
        print(f"{i} -- f({x0}) = {fx0} -- exact root")
    else:
        abs_err = tol + 1
        rel_err = abs_err
        error = abs_err

        print(f"{i} -- f({x0}) = {fx0} -- abs_err = {abs_err} -- rel_err = {rel_err}")

        fx1 = f(x1)
        denominator = fx1 - fx0
        i = i + 1
        while error > tol and fx1 != 0 and denominator != 0 and i < n:
            print(
                f"{i} -- f({x1}) = {fx1} -- abs_err = {abs_err} -- rel_err = {rel_err}"
            )

            x2 = x1 - ((fx1 * (x1 - x0)) / denominator)
            abs_err = abs(x2 - x1)
            rel_err = abs_err / abs(x2)

            if with_abs_err:
                error = abs_err
            else:
                error = rel_err

            x0 = x1
            fx0 = fx1
            x1 = x2
            fx1 = f(x1)
            denominator = fx1 - fx0
            i = i + 1

    if fx1 == 0:
        print(f"{i} -- f({x1}) = {fx1} -- exact root")
    elif error < tol:
        print(f"{i} -- f({x1}) = {fx1} -- asb_err = {abs_err} -- rel_err = {rel_err}")
    elif denominator == 0:
        print("possibly a multiple root")
    else:
        print(f"{i} -- Failed")
