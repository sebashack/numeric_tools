from collections import namedtuple

Si = namedtuple("Si", "ai bi xi")


def linear_splines(points):
    points_ = sorted(points)
    equations = []
    intervals = []
    for p0, p1 in zip(points_, points_[1:]):
        x0, f0 = p0
        x1, f1 = p1
        b = (f1 - f0) / (x1 - x0)
        intervals.append((x0, x1))
        equations.append(Si(f0, b, x0))
    return (equations, intervals)


def linear_eqs_strs(eqs, intervals):
    eq_ss = []
    for i, (eq, intv) in enumerate(zip(eqs, intervals)):
        s = f"s{i} = {eq.ai} + {eq.bi}(x - {eq.xi}), [{intv[0]},{intv[1]}]"
        eq_ss.append(s)

    return eq_ss
