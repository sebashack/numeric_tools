import sys
import math

from incremental_search import incremental_search
from bisection import bisection


def main(argv):
    def g(x):
        v = math.pow(x, 3) - (7.5 * math.pow(x, 2)) + (18.4239 * x) - 14.8331
        return v

    def f(x):
        v = math.pow(math.e, (3 * x) - 12) + (x * math.cos(3 * x)) - math.pow(x, 2) + 4
        return v

    # incremental_search(f, -10, 1, 240)
    bisection(g, 3, 3.5, (5 * math.pow(10, -5)))


if __name__ == "__main__":
    main(sys.argv[1:])
