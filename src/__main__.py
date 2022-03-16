import sys
import math

from bisection import bisection
from false_rule import false_rule
from incremental_search import incremental_search
from fixed_point import fixed_point


def main(argv):
    def g(x):
        v = math.pow(x, 3) - (7.5 * math.pow(x, 2)) + (18.4239 * x) - 14.8331
        return v

    def f(x):
        v = math.pow(math.e, (3 * x) - 12) + (x * math.cos(3 * x)) - math.pow(x, 2) + 4
        return v

    # incremental_search(f, -10, 1, 240)
    # bisection(f, 2, 3, (0.5 * math.pow(10, -3)), True)
    bisection(f, 2, 3, (5 * math.pow(10, -10)), False)
    false_rule(f, 2, 3, (5 * math.pow(10, -10)), False)

    # def w(x):
    #     v = (x * math.pow(math.e, x)) - math.pow(x, 2) - (5 * x) - 3
    #     return v

    # def h(x):
    #     v = (x * math.pow(math.e, x)) - math.pow(x, 2) - 3
    #     return v / 5

    # fixed_point(w, h, -0.5, 5 * math.pow(10, -5), 10, False)


if __name__ == "__main__":
    main(sys.argv[1:])
