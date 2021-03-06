# err_type = abs | rel | fx
def bisection(f, xlo, xup, tol, err_type="abs"):
    fxlo = f(xlo)
    fxup = f(xup)
    i = 0

    if fxlo == 0:
        return xlo
    elif fxup == 0:
        return xup
    elif fxlo * fxup < 0:
        xm = (xlo + xup) / 2
        fxm = f(xm)
        i = 1
        abs_err = float("inf")
        rel_err = float("inf")
        error = float("inf")

        if err_type == "fx":
            error = abs(fxm)

        while error >= tol and fxm != 0:
            if fxlo * fxm < 0:
                xup = xm
                fxup = fxm
            elif fxm * fxup < 0:
                xlo = xm
                fxlo = fxm

            xtemp = xm
            xm = (xlo + xup) / 2
            fxm = f(xm)
            abs_err = abs(xm - xtemp)
            rel_err = abs_err / abs(xm)

            if err_type == "fx":
                error = abs(fxm)
            elif err_type == "rel":
                error = rel_err
            else:
                error = abs_err

            i = i + 1

        if fxm == 0 or error < tol:
            return xm
    else:
        return None
