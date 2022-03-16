def bisection(f, xlo, xup, tol, with_abs_err=True):
    fxlo = f(xlo)
    fxup = f(xup)
    i = 0

    if fxlo == 0:
        print(f"{i} -- f({xlo}) = {fxlo}")
    elif fxup == 0:
        print(f"{i} -- f({xup}) = {fxup}")
    elif fxlo * fxup < 0:
        xm = (xlo + xup) / 2
        fxm = f(xm)
        i = 1
        abs_err = tol + 1
        rel_err = abs_err
        error = abs_err

        while error >= tol and fxm != 0:
            # print(f"{i} -- f({xm}) = {fxm} -- err = {abs_err} -- rel_err = {rel_err}")
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

            if with_abs_err:
                error = abs_err
            else:
                error = rel_err

            i = i + 1

        if fxm == 0:
            print(f"{i} -- f({xm}) = {fxm} -- exact root")
        elif error < tol:
            print(f"{i} -- f({xm}) = {fxm} -- err = {abs_err} -- rel_err = {rel_err}")
    else:
        print("Invalid interval")
