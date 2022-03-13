import math


def false_rule(f, xlo, xup, tol):
    fxlo = f(xlo)
    fxup = f(xup)
    i = 0

    if fxlo == 0:
        print(f"{i} -- f({xlo}) = {fxlo}")
    elif fxup == 0:
        print(f"{i} -- f({xup}) = {fxup}")
    elif fxlo * fxup < 0:
        xm = xlo - ((fxlo * (xup - xlo)) / (fxup - fxlo))
        fxm = f(xm)
        i = 1
        error = tol + 1

        while error >= tol and fxm != 0:
            if fxlo * fxm < 0:
                xup = xm
                fxup = fxm
            elif fxm * fxup < 0:
                xlo = xm
                fxlo = fxm

            xtemp = xm
            xm = xlo - ((fxlo * (xup - xlo)) / (fxup - fxlo))
            fxm = f(xm)
            error = abs(xm - xtemp)
            i = i + 1

        if fxm == 0:
            print(f"{i} -- f({xm}) = {fxm} -- exact root")
        elif error < tol:
            print(f"{i} -- f({xm}) = {fxm} -- error = {error}")
    else:
        print("Invalid interval")
