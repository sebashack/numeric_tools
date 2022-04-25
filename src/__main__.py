import sys
import math

from matrix_utils import set_print_opts, mkMat, mkVec
from simple_gaussian_elim import simple_gaussian_elim
from regressive_substitution import regressive_substitution

set_print_opts(3)


def main(argv):
    a = mkMat([[2, -1, -3, 2], [5, -10, 2, -6], [5, -9, 15, -6], [2, 1, -1, 10]])
    b = mkVec([4, 3, 2, 1])
    ab = simple_gaussian_elim(a, b)
    xs = regressive_substitution(ab)
    print(ab)
    print(xs)


if __name__ == "__main__":
    main(sys.argv[1:])
