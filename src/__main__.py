import sys
import math

from bisection import bisection
from false_rule import false_rule
from fixed_point import fixed_point
from fun_plot import plot
from incremental_search import incremental_search
from maximum_dg import maximum_dg
from newton import newton
from secant import secant
from multiple_roots import multiple_roots


def main(argv):
    def g(x):
        return math.pow(math.e, -x)

    def dg(x):
        return -math.pow(math.e, -x)

    def f(x):
        return math.pow(math.e, -x) - x

    def df(x):
        return -math.pow(math.e, -x) - 1

    def ddf(x):
        return -math.pow(math.e, x)

    tolerance = math.pow(10, -4)
    secant(f, (0, 1), tolerance, 100, err_type="fx")
    print("----")
    multiple_roots(f, df, ddf, 0, tolerance, 100, err_type="fx")
    print("----")
    newton(f, df, 0, tolerance, 100, err_type="fx")
    print("----")
    fixed_point(f, g, dg, 0, tolerance, 100, err_type="rel")
    print("----")
    false_rule(f, 0, 0.6, tolerance, err_type="fx")
    print("----")
    bisection(f, 0, 0.6, tolerance, err_type="rel")
    print("----")
    incremental_search(f, 0, 0.001, 1000)


if __name__ == "__main__":
    main(sys.argv[1:])
