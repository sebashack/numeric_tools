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
        return math.pow(math.e, -x)

    tolerance = 5 * math.pow(10, -5)
    print(secant(f, (-1, 1), tolerance, 100, err_type="fx"))
    print("----")
    print(multiple_roots(f, df, ddf, -1, tolerance, 100, err_type="fx"))
    print("----")
    print(newton(f, df, -2, tolerance, 100, err_type="abs"))
    print("----")
    print(fixed_point(f, g, 0, tolerance, 100, err_type="abs"))
    print("----")
    print(false_rule(f, -2, 5.0, tolerance, err_type="abs"))
    print("----")
    print(bisection(f, -2, 5.0, tolerance, err_type="abs"))
    print("----")
    print(incremental_search(f, 0, 0.00001, 100000))


if __name__ == "__main__":
    main(sys.argv[1:])
