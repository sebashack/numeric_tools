import matplotlib as mpl
import matplotlib.pyplot as plt
import math


def plot(interval, dx, f=None, g=None):
    fig, xy = plt.subplots()

    d = abs(interval[1] - interval[0])
    n = math.ceil(d / dx)

    if f is not None:
        xs = [interval[0]]
        fxs = [f(interval[0])]

        for i in range(0, n):
            xs.append(xs[i] + dx)
            fxs.append(f(xs[i] + dx))

        xy.plot(xs, fxs, "r")

    if g is not None:
        vs = [interval[0]]
        gvs = [g(interval[0])]

        for i in range(0, n):
            vs.append(vs[i] + dx)
            gvs.append(g(vs[i] + dx))

        xy.plot(vs, gvs, "b")

    xy.plot(interval, [0, 0], "k")

    plt.show()
