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


def main(argv):
    def f(x):
        return math.pow(math.e, -x) - x

    def g(x):
        return math.pow(math.e, x) - (5 * x) + 2

    tolerance = 0.5 * math.pow(10, -10)
    secant(g, (0.5, 1), tolerance, 20, True)


if __name__ == "__main__":
    main(sys.argv[1:])
