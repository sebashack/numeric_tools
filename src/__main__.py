import sys
import math

from bisection import bisection
from false_rule import false_rule
from incremental_search import incremental_search
from fixed_point import fixed_point
from fun_plot import plot
from maximum_dg import maximum_dg


def main(argv):
    # def f(x):
    #     v = math.pow(x, 3) + (2 * math.pow(x, 2)) + (10 * x) - 20
    #     return v

    # def g(x):
    #     d = math.pow(x, 2) + (2 * x) + 10
    #     return 20 / d

    # fixed_point(f, g, 0, math.pow(10, -6), 100, True)

    def f(x):
        v = math.pow(x, 2) - (2 * x) + 2 - math.pow(math.e, x)
        return v

    def df(x):
        v = (2 * x) - 2 - math.pow(math.e, x)
        return v

    def g(x):
        v = math.pow(x, 2) - (2 * x) + 2
        return math.log(v)

    def dg(x):
        a = (2 * x) - 2
        b = math.pow(x, 2) - (2 * x) + 2
        return a / b

    tolerance = 0.5 * math.pow(10, -4)
    fixed_point(f, g, dg, 0.5, tolerance, 100, True)
    print(maximum_dg((0.1, 0.6), 0.001, dg))


if __name__ == "__main__":
    main(sys.argv[1:])
