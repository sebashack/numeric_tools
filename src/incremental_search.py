def incremental_search(f, xinit, dx, n):
    x0 = xinit
    fx0 = f(x0)

    if fx0 == 0:
        print(f"0 -- root({x0})")
    else:
        i = 1
        x1 = x0 + dx
        fx1 = f(x1)

        # while fx0 * fx1 > 0 and i < n:
        while i < n:
            x0 = x1
            x1 = x0 + dx

            fx0 = fx1
            fx1 = f(x1)

            print_root(i, x0, fx0, x1, fx1)

            i = i + 1


def print_root(i, x0, fx0, x1, fx1):
    if fx1 == 0:
        print(f"{i} -- f({x1}) = {fx1}")
    elif fx0 * fx1 < 0:
        print(f"{i}--| {x0}, {x1} | f(x0)={fx0}, f(x1)={fx1} |")
