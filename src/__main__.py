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
    def f(x):
        ex = math.pow(math.e, x)
        return (x * ex) - ex + 1

    def df(x):
        return x * math.pow(math.e, x)

    def ddf(x):
        ex = math.pow(math.e, x)
        return (x * ex) + ex

    tolerance = math.pow(10, -5)
    multiple_roots(f, df, ddf, 0.5, tolerance, 5, err_type="abs")


if __name__ == "__main__":
    main(sys.argv[1:])
