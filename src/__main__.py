import sys
import math

from incremental_search import incremental_search


def main(argv):
    def f(x):
        v = math.pow(x, 3) - math.pow(x, 2) + (3 * x) - 2
        return v

    incremental_search(f, 0, 0.001, 100000)


if __name__ == "__main__":
    main(sys.argv[1:])
